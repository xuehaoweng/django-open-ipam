# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
import logging
import os
import time
from datetime import datetime, timedelta

from celery import shared_task, current_app
from ipam_boost.celery import IpAmTask
from open_ipam.models import IpAddress, Subnet, BgBu
from utils.ipam_utils import IpAmForNetwork
from utils.mongo_api import IpamOps
from ipam_boost.settings_dev import BASE_DIR
from netaddr import IPNetwork, IPSet


def write_log(filename, datas):
    try:
        isExists = os.path.exists(os.path.dirname(filename))
        if not isExists:
            os.makedirs(os.path.dirname(filename))
    except Exception as e:
        pass
    with open(filename, 'a', encoding='utf-8-sig') as f:
        for row in datas:
            f.write(row)
    print('Write Log Done!')


@shared_task(base=IpAmTask, once={'graceful': True})
def get_all_tasks():
    celery_app = current_app
    # celery_tasks = [task for task in celery_app.tasks if not task.startswith('celery.')]
    res = list(sorted(name for name in celery_app.tasks
                      if not name.startswith('celery.')))
    return json.dumps({'result': res})


@shared_task(base=IpAmTask, once={'graceful': True})
def ipam_scan():
    pass


@shared_task(base=IpAmTask, once={'graceful': True})
def ip_am_update_sub_task(ip):
    # 获取地址表实例
    ip_address_model = IpAddress
    # 文件名-操作失败的IP地址写入文件中
    file_time = datetime.now().strftime("%Y-%m-%d")
    # 地址操作失败保存文件路径.log
    ip_am_ip_fail_file = os.path.join(BASE_DIR, 'media', 'ipam', "netaxe_ipam_ip_fail-{}.log".format(file_time))
    # 在网络地址表取地址实例
    ip_address_instance = ip_address_model.objects.filter(ip_address=ip).values().first()
    # 预先定义初始化desc
    tmp_description = {"Last Online Time": file_time, "BgBu": '[]'}
    # 最近在线时间
    lastOnlineTime = file_time

    # TODO 判断IP地址是否在NetAxe-IPAM中有记录

    # IP地址暂时不存在IPAM中 则不存在子网网段IP
    if ip_address_instance is None:
        # 地址不存在,则去判断16位网段存不存在,看是否需要先新增网段
        subnet16_id = IpAmForNetwork.get_sixteen_subnet_id(ip=ip)
        if subnet16_id:
            subnet24 = IPNetwork(f'{ip}/24').network
            print("subnet24", str(subnet24) + "/24")
            # 查询当前IP是否存在24位网段
            subnet24_instance = Subnet.objects.filter(subnet=str(subnet24) + "/24").first()
            if subnet24_instance:
                # ip归属子网ID为24位网段id
                subnet_insert_id = subnet24_instance.id
            else:
                # 新建24位网段
                subnet_instance = Subnet(subnet=str(subnet24) + "/24", mask=24, master_subnet_id=subnet16_id,
                                         description=f'netaxe_ipam {file_time} 新建网段')

                subnet_instance.save()
                # ip归属子网ID为 TODO 新建24位网段id
                subnet_insert_id = subnet_instance.id

            """
            # 新增IP地址信息置位tag=4  未分配已使用
            1、查询除log_time字段外，是否有完全匹配，如果有就只更新log_time字段, 如果log_time字段一致，则不进行任何操作
            2、如果查询不到数据，则新增该字段
            """
            # TODO 到新增地址表
            IpamOps.post_success_ip(ip)
            ip_create_instance = IpAddress(subnet_id=subnet_insert_id, ip_address=ip, tag=4,
                                           description=json.dumps(tmp_description))
            ip_create_instance.save()
        # 若不存在16位网段
        else:
            # 不存在16位网段-直接 TODO 丢弃到失败列表
            print('请先创建此IP归属网段：{}'.format(ip))
            IpamOps.post_fail_ip(ip)
            _tmp_data = []
            _tmp_data.append(ip + '\n')
            write_log(ip_am_ip_fail_file, _tmp_data)


    else:
        ip_address_id = ip_address_instance['id']
        ip_address_tag = ip_address_instance['tag']
        ip_address_desc = ip_address_instance['description']
        bgbu_id_list = []
        if ip_address_desc != "":
            ip_address_desc = eval(ip_address_desc)
            if 'BgBu' in ip_address_desc.keys() and ip_address_desc['BgBu'] != "[]":
                bgbu_name_list = ip_address_desc['BgBu']
                if len(bgbu_name_list) > 0:
                    for bgbu_name in bgbu_name_list:
                        if type(bgbu_name) == int:
                            bgbu_id = bgbu_name
                        else:
                            try:
                                bgbu_id = BgBu.objects.filter(name=bgbu_name).values().first()['id']
                            except Exception as e:
                                # 新增bgbu
                                bgbu_instance = BgBu(name=bgbu_name)
                                bgbu_instance.save()
                                bgbu_id = bgbu_instance.id
                        bgbu_id_list.append(bgbu_id)
        if ip_address_tag == 6:  # 已分配未使用变更到已分配已使用、最近在线时间、描述信息、BgBu
            # TODO 更新 6>> 2
            IpamOps.post_update_ip(ip)
            ip_update_6_instance = IpAddress.objects.get(id=ip_address_id)
            ip_update_6_instance.tag = 2
            ip_update_6_instance.lastOnlineTime = lastOnlineTime
            ip_update_6_instance.description = tmp_description
            ip_update_6_instance.bgbu.set(bgbu_id_list)
            ip_update_6_instance.save()
        if ip_address_tag == 7:  # 自定义空闲变更到未分配已使用、最近在线时间、描述信息、BgBu
            # TODO 更新 7>> 4
            IpamOps.post_update_ip(ip)
            ip_update_7_instance = IpAddress.objects.get(id=ip_address_id)
            ip_update_7_instance.tag = 4
            ip_update_7_instance.lastOnlineTime = lastOnlineTime
            ip_update_7_instance.description = tmp_description
            ip_update_7_instance.bgbu.set(bgbu_id_list)
            ip_update_7_instance.save()
        else:  # 更新tag、最近在线时间、描述信息、BgBu
            # TODO 更新 未使用-仅更新在线时间、描述信息、BGBU等
            IpamOps.post_update_ip(ip)
            ip_update_else_instance = IpAddress.objects.get(id=ip_address_id)
            ip_update_else_instance.tag = ip_address_tag
            ip_update_else_instance.lastOnlineTime = lastOnlineTime
            ip_update_else_instance.description = tmp_description
            ip_update_else_instance.bgbu.set(bgbu_id_list)
            ip_update_else_instance.save()

    return


# IPAM地址全网更新main
@shared_task(base=IpAmTask, once={'graceful': True})
def ip_am_update_main():
    start_time = time.time()
    print("IPAM地址信息更新开始")
    file_time = datetime.now().strftime("%Y-%m-%d")
    # 获取tasks任务数量
    ip_am_update_tasks = []
    # 获取现网中所有IP地址 Total_ip_list
    total_ip = IpamOps.get_total_ip()
    ip_am_ip_fail_file = os.path.join(BASE_DIR, 'media', 'ipam', "netops_ipam_ip_fail-{}.log".format(file_time))
    # 删除旧数据库
    if total_ip:
        IpamOps.delet_coll(coll='netaxe_ipam_fail_ip')
        IpamOps.delet_coll(coll='netaxe_ipam_success_ip')
        IpamOps.delet_coll(coll='netaxe_ipam_update_ip')
    else:
        print("IPAM地址信息更新失败：未获取到total_ip_list")
        return
    for ip_info in total_ip:
        if ip_info['ipaddress']:
            # print(ip_info['ipaddress'])
            # 异步函数方式-验证中
            ip_am_update_tasks.append(
                ip_am_update_sub_task.apply_async(args=(ip_info['ipaddress'],), queue='netaxe_ipam'))

            # ip_am_update_sub_task(ip_info['ipaddress'])
    print("子任务下发完毕")

    # 等待子任务全部执行结束后执行下一步
    while len(ip_am_update_tasks) != 0:
        for tasks in ip_am_update_tasks:
            if tasks.ready():
                ip_am_update_tasks.remove(tasks)
    print('子任务执行完毕')
    total_time = int((time.time() - start_time) / 60)
    print('花费总时间', total_time)

    ip_fail_counts = IpamOps.get_coll_account(coll='netaxe_ipam_fail_ip')  # 失败地址表
    ip_add_counts = IpamOps.get_coll_account(coll='netaxe_ipam_success_ip')  # 新增地址表
    ip_update_counts = IpamOps.get_coll_account(coll='netaxe_ipam_update_ip')  # 更新地址表

    # # 发送邮件和微信信息
    send_message = 'PAM地址信息更新完成!\n新录入成功: {}个\n新录入失败: {}个\n更新成功: {}个\n总耗时: {}分钟\n'.format(
        ip_add_counts, ip_fail_counts, ip_update_counts, total_time)

    try:
        print(send_message)
    except Exception as e:
        pass
    print("发送微信、邮件完毕")

    return


# 定时回收地址
# 讯飞云地址不回收？
'''
# 子网白名单
 "172.22.143.0/24",  # 音乐服务
 "172.22.144.0/24",  # 音乐服务
 "172.22.145.0/24",  # 音乐服务
 "172.22.98.0/24",  # 音乐服务
 "172.22.104.0/24",  # 音乐服务
 "172.22.149.0/24",  # 阅读
 172.22.149.0/24",  # 阅读
'''


@shared_task(base=IpAmTask, once={'graceful': True})
def recycle_ip_main():
    today_date = datetime.now().strftime("%Y-%m-%d")

    nine_days_ago_date = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")
    # 最近在线时间为90天之前
    recycle_ip_list = IpAddress.objects.filter(lastOnlineTime__lt=nine_days_ago_date)
    for recycle in recycle_ip_list:
        recycle.tag = 1
    pass
