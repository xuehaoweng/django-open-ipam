from django.contrib import admin

# Register your models here.
from django.contrib.admin.models import LogEntry

from users.models import UserProfile, OpLogs, AccessTimeOutLogs


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'nick_name', 'mobile', 'get_login_status', 'email']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('bgbu')
        return queryset


class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message', 'object_repr']
    list_filter = ('user', 'action_flag')
    search_fields = ['action_flag', 'user', 'change_message']


admin.site.register(LogEntry, LogEntryAdmin)


@admin.register(OpLogs)
class OpLogsAdmin(admin.ModelAdmin):
    list_display = ['re_url', 're_method', 'access_time', 're_ip', 'user_agent', 'rp_code', 're_content', 're_time',
                    're_user',
                    ]  # rp_content 响应参数内容太多不展示
    list_filter = ('re_url', 're_user')
    search_fields = ['re_url', 're_user', 'rp_code']


@admin.register(AccessTimeOutLogs)
class AccessTimeOutLogsAdmin(admin.ModelAdmin):
    list_display = ['re_url', 're_method', 'access_time', 're_ip', 'user_agent', 'rp_code', 're_content', 're_time',
                    're_user',
                    ]  # rp_content 响应参数内容太多不展示
    list_filter = ('re_url', 're_user')
    search_fields = ['re_url', 're_user', 'rp_code']
