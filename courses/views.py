from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Course


class CourseListView(View):
    """
    课程列表视图
    """
    def get(self, request):
        current_page = 'course_list'
        courses = Course.objects.all()
        return render(request, 'course-list.html', {
            'courses': courses,
            'current_page': current_page,
        })


class CourseDetailView(View):
    """
    课程详情视图
    """
    def get(self, request, course_id):
        course = get_object_or_404(Course, id=int(course_id))
        videos = course.videos.all()
        fake_videos = [fake_video for fake_video in range(1, 15)]
        return render(request, 'course-detail.html', {
            'course': course,
            'videos': videos,
            'fake_videos': fake_videos,
        })