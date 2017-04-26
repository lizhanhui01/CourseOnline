# _*_ encoding:utf-8 _*_
from django.contrib import admin

# Register your models here.
# 用于注册后台管理系统

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile,UserProfileAdmin)