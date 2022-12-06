#!/bin/bash
cd /home/netaxeipam
python3 manage.py collectstatic
web(){
    mkdir -p /home/netaxeipam/logs/celery_logs
    mkdir -p /var/log/supervisor
    rm -rf /home/netaxeipam/logs/celery_logs/w*.log
    rm -rf *.pid
    echo 'uwsgi done'
    supervisord -n -c /home/netaxeipam/supervisord_prd.conf
}
netaxe_ipam(){
    sleep 10
    celery -A ipam_boost worker -Q netaxe_ipam -c 10 -l info -n netaxe_ipam
}
case "$1" in
web)
web
;;
netaxe_ipam)
netaxe_ipam
;;
*)
echo "Usage: $1 {web|netaxe_ipam}"
;;
esac
echo "start running!"