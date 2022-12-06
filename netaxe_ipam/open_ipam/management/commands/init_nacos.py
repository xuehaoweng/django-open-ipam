# -*- coding: utf-8 -*-

from utils.nacos import nacos
from ipam_boost.conf import SERVERIP, SERVICEPORT

# 注册服务
nacosServer = nacos(ip=SERVERIP, port=8848)
nacosServer.registerService(
    serviceIp=SERVERIP,  # 当前微服务ip、此时宿主机保持一致
    servicePort=SERVICEPORT,  # 当前微服务暴露端口
    serviceName="auth",
    groupName="default")
nacosServer.healthyCheck()
