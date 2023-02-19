#!/bin/bash
cd /home/django_openipam
python3 manage.py collectstatic
web(){
    mkdir -p /home/django_openipam/logs/celery_logs
    mkdir -p /var/log/supervisor
    rm -rf /home/django_openipam/logs/celery_logs/w*.log
    rm -rf *.pid
    echo 'uwsgi done'
    supervisord -n -c /home/django_openipam/supervisord_prd.conf
}
django_open_ipam(){
    sleep 10
    celery -A ipam_boost worker -Q django_open_ipam -c 10 -l info -n django_open_ipam
}
case "$1" in
web)
web
;;
django_open_ipam)
django_open_ipam
;;
*)
echo "Usage: $1 {web|django_open_ipam}"
;;
esac
echo "start running!"