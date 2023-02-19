#!/bin/bash
cd /home/django_openipam && git pull
pip3 install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py init_users
echo "system init success!"