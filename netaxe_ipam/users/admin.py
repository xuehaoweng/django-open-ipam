from django.contrib import admin

# Register your models here.
from users.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'nick_name', 'mobile', 'get_login_status', 'email']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('bgbu')
        return queryset
