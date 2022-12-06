# -*- coding: utf-8 -*-

from utils.nacos import nacos
from ipam_boost.conf import SERVER_IP, SERVICE_PORT

# 注册服务
nacosServer = nacos(ip=SERVER_IP, port=8848)
nacosServer.registerService(
    serviceIp=SERVER_IP,  # 当前微服务ip、此时宿主机保持一致
    servicePort=SERVICE_PORT,  # 当前微服务暴露端口
    serviceName="ipam",
    groupName="default")
nacosServer.healthyCheck()
