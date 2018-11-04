# encoding: utf-8
"""
@author: Sunmouren
@contact: sunxuechao1024@gmail.com
@time: 2018/11/2 12:36
@desc: 
"""

from django.urls import path
from .views import UserLogoutView, UserProfileView, UserLoginView, UserRegisterView

app_name = 'users'


urlpatterns =[
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(),  name='user_logout'),
    path('profile/<int:user_id>/', UserProfileView.as_view(), name='user_profile'),
    path('register/', UserRegisterView.as_view(), name='user_register'),
]