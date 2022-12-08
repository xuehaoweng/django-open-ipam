"""IpamV1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework.documentation import include_docs_urls
from django.views.static import serve
from ipam_boost.views import obtain_expiring_auth_token, page_not_found
from ipam_boost import settings
from open_ipam.tolls.login import LoginView

urlpatterns = [
    path(r'ipam/docs/', include_docs_urls(title='NetOpsIpam接口文档')),
    path('ipam/admin/', admin.site.urls),
    path('ipam/login/', LoginView.as_view(), name="login"),
    path(r'ipam/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'ipam/api-token/', obtain_expiring_auth_token, name='api-token'),
    path(r'ipam/v1/', include('open_ipam.urls'), ),
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
]

handler404 = page_not_found
