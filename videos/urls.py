# encoding: utf-8
"""
@author: Sunmouren
@contact: sunxuechao1024@gmail.com
@time: 2018/10/26 21:24
@desc: 
"""

from django.urls import path

from .views import VideoDetailView, AddVideoView, uptoken


app_name = 'videos'

urlpatterns = [
    path('detail/<int:vid>/', VideoDetailView.as_view(), name='videos_detail'),
    path('add/', AddVideoView.as_view(), name='add_video'),
    path('uptoken/', uptoken),
]