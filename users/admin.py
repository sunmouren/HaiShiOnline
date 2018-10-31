from django.contrib import admin

from .models import UserProfile, FollowUser


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    用户后台管理
    """
    list_display = ['username', 'email', 'avatar', 'date_joined']
    list_filter = ['username', 'email', 'date_joined']
    search_fields = ['username', 'email']


@admin.register(FollowUser)
class FollowUserAdmin(admin.ModelAdmin):
    """
    用户关注管理
    """
    list_display = ['user_from', 'user_to', 'created']
    search_fields = ['user_from', 'user_to']
    list_filter = ['created']
