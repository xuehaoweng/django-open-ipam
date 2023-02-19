# -*- coding: utf-8 -*-
import json
import os
import django
from django.core.management import BaseCommand

# from open_ipam.models import BgBu

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ipam_boost.settings')
django.setup()
from ipam_boost.settings_dev import BASE_DIR
from django.apps import apps


# from apps.asset.models import Idc


def main():
    with open(os.path.join(BASE_DIR, 'utils', 'init_users.json'), 'r', encoding="utf-8") as load_f:
        code_list = json.load(load_f)
        for table, values in code_list.items():
            my_model = apps.get_model("users", table)
            if my_model:
                for value in values:
                    print(table, value)
                    # if table == "BgBu":
                    #     value['id'] = BgBu.objects.get(id=value['id'])
                    my_model.objects.get_or_create(**value)


class Command(BaseCommand):
    """
    项目初始化命令: python manage.py init_bgbu
    """

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print(f"正在准备初始化用户数据...")
        main()
        print("数据初始化用户数据完成！")
