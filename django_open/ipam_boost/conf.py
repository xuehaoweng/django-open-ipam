
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
SERVER_IP = "10.254.0.111"
SERVICE_PORT = "38001"

# REDIS_URL = "redis://:dade0f2a65237a56b79277e6dd27351d2854df033e0ad4b4f90abec229cd64df@redis-cache:6379/"
REDIS_URL = "redis://:dade0f2a65237a56b79277e6dd27351d2854df033e0ad4b4f90abec229cd64df@{}:6379/".format(SERVER_IP)
CACHE_PWD = ''
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
    'username': 'admin',
    'password': 'djangoopenadmin',
}
