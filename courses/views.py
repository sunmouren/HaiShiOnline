from django.shortcuts import render
from django.views.generic import View

from .models import Course


class CourseListView(View):
    """
    课程列表视图
    """
    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'course-list.html', {'courses', courses})