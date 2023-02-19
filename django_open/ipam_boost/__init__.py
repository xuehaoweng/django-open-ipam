import pymysql

from ipam_boost import settings_dev

# from utils.nacos import nacos

pymysql.version_info = (1, 4, 2, "final", 0)
pymysql.install_as_MySQLdb()
