import pymysql

from ipam_boost import settings_dev

# from utils.nacos import nacos

pymysql.version_info = (1, 4, 2, "final", 0)
pymysql.install_as_MySQLdb()

# nacosServer = nacos(ip=settings.nacos_server_ip, port=8848)
# nacosServer.registerService(serviceIp=settings.local_service_ip, servicePort=settings.local_service_port, serviceName="ipam",
#                             groupName="default")
# nacosServer.healthyCheck()
