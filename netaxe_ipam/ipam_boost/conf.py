# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      conf
   Description:
   Author:          Lijiamin
   date：           2022/7/28 14:59
-------------------------------------------------
   Change Activity:
                    2022/7/28 14:59
-------------------------------------------------
"""
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
SERVER_IP = "10.254.2.219"
SERVICE_PORT = "38001"
DATABASES = {
    'default': {
        'NAME': 'netaxe_ipam',
        'ENGINE': 'django.db.backends.mysql',
        'HOST': SERVER_IP,
        'USER': 'root',
        'PASSWORD': 'root_devnet@2022',
        'PORT': '3306',
        'CONN_MAX_AGE': 21600,
        'ATOMIC_REQUESTS': True,
        'TEST_CHARSET': 'utf8mb4',
        'TEST_COLLATION': 'utf8mb4_general_ci',
        'TEST': {'NAME': 'net_axe_test',
                 'CHARTSET': 'utf8mb4',
                 'COLLATION': 'utf8mb4_general_ci'},
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    },
}

# REDIS_URL = "redis://:dade0f2a65237a56b79277e6dd27351d2854df033e0ad4b4f90abec229cd64df@redis-cache:6379/"
REDIS_URL = "redis://:dade0f2a65237a56b79277e6dd27351d2854df033e0ad4b4f90abec229cd64df@{}:6379/".format(SERVER_IP)
CACHE_PWD = 'dade0f2a65237a56b79277e6dd27351d2854df033e0ad4b4f90abec229cd64df'
mongo_db_conf = {
    "host": SERVER_IP,
    "port": 27017,
    "username": "root",
    "password": "70uUceCVL1gf"
}
netops_api = {
    "token_url": 'http://{}:9999/api/token/'.format(SERVER_IP),
    "base_url": 'http://{}:9999/api/'.format(SERVER_IP),
    "resources_manage_base_url": 'http://{}:9999/resources_manage/api/'.format(SERVER_IP),
    'username': 'adminnetaxe',
    'password': 'netaxeadmin',
}
