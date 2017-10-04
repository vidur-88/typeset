"""typeset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
# from django.contrib import admin
# from django.contrib.auth.models import User, Group

#
# class AccessUser:
#     has_module_perms = has_perm = __getattr__ = lambda s,*a,**kw: True
#
# admin.site.has_permission = lambda r: setattr(r, 'user', AccessUser()) or True
# admin.site.unregister(User)
# admin.site.unregister(Group)
#
# try:
#     User.objects.get_by_natural_key('admin')
# except User.DoesNotExist:
#     User.objects.create_superuser('admin', 'admin@optibus.co', '123456')

urlpatterns = [
    url(r'^blogs/', include('blogs.urls')),
    # url(r'^admin/', include(admin.site.urls)),
]
