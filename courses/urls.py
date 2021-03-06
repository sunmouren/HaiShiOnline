# encoding: utf-8
"""
@author: Sunmouren
@contact: sunxuechao1024@gmail.com
@time: 2018/10/30 19:20
@desc: 
"""

from django.urls import path

from .views import CourseListView, CourseDetailView


app_name = 'courses'


urlpatterns = [
    path('list/', CourseListView.as_view(), name='course_list'),
    path('detail/<int:course_id>/', CourseDetailView.as_view(), name='course_detail'),
]