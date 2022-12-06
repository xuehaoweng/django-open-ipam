from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class UserProfile(AbstractUser):
    login_status_ = (
        (0, '在线'),
        (1, '离线'),
        (2, '忙碌'),
        (3, '离开'),
    )
    nick_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='昵称')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号码')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', default='images/default.png', max_length=100)
    login_status = models.SmallIntegerField(choices=login_status_, default=1, verbose_name='登录状态')
    bgbu = models.ManyToManyField("open_ipam.BgBu", verbose_name='BGBU', blank=True)

    # role =

    def bgbu_list(self):
        return ','.join([i.name for i in self.bgbu.all()])

    def get_login_status(self):
        return self.login_status

    class Meta:
        db_table = 'ipam_user'
        verbose_name = '用户表'
        verbose_name_plural = '用户表'
