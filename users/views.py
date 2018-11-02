from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth import logout
from django.urls import reverse

from .models import UserProfile


class UserLogoutView(View):
    """
    退出登录
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class UserProfileView(View):
    """
    用户主页
    """
    def get(self, request, user_id):
        user = get_object_or_404(UserProfile, id=int(user_id))
        info = '我' if request.user == user else 'TA'
        return render(request, 'user-profile.html', {
            'user': user,
            'info': info,
        })