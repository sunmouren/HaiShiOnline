import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View


from courses.models import Course


from qiniu import Auth

from .models import Video
from .forms import VideoForm


BUCKET_NAME = "hsonline"
ACCESS_KEY = "5fCtYuw72dt7UZiL3G1GWROtl-GTVC5bYYDVdhRI"
SECRET_KEY = "g1DKeYcCPop64IkcrOzHIr1S011MJ6x74MqXFvSu"


def uptoken(request):
    """
    生成七牛云的 uptoken
    :param request:
    :return:
    """
    q = Auth(ACCESS_KEY, SECRET_KEY)
    token =q.upload_token(bucket=BUCKET_NAME, key=None, expires=3600)
    data = {'uptoken': token}
    return HttpResponse(json.dumps(data), content_type="application/json")


class VideoDetailView(View):
    """
    视频详情
    """
    def get(self, request, vid):
        video = get_object_or_404(Video, id=int(vid))
        comments = video.video_comments.order_by('-like_number')

        return render(request, 'video-detail.html', {
            'video': video,
            'comments': comments,
        })


class AddVideoView(LoginRequiredMixin, View):
    """
    添加视频
    """
    def get(self, request):
        current_page = 'add_video'
        courses = Course.objects.filter(user=request.user)
        return render(request, 'add-video.html', {
            'current_page': current_page,
            'courses': courses,
        })

    def post(self, request):
        video_form = VideoForm(data=request.POST)
        if video_form.is_valid():
            try:
                new_video = video_form.save(commit=False)
                new_video.user = request.user
                new_video.save()
                return render(request, 'add-video.html')
            except BaseException as e:
                print('upload error {0}'.format(e))
        return render(request, 'add-video.html')



