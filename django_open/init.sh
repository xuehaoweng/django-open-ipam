#!/bin/bash
cd /home/django_openipam && git pull
pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
python manage.py makemigrations
python manage.py migrate

python manage.py init_users
echo "system init success!"