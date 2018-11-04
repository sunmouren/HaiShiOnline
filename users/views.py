from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth import logout, authenticate, login
from django.urls import reverse

from courses.models import Course
from videos.forms import UserRegisterForm
from videos.models import Video

from .models import UserProfile
from .forms import UserLoginForm


class UserProfileView(View):
    """
    用户主页
    """
    def get(self, request, user_id):
        user = get_object_or_404(UserProfile, id=int(user_id))
        user_flag = '我' if request.user == user else 'TA'
        # 根据data获取相应的用户data模块, 默认为 ’courses'
        data = request.GET.get('data', 'courses')
        objects = self.get_objects(user=user, data=data)
        return render(request, 'user-profile.html', {
            'user': user,
            'objects': objects,
            'data': data,
            'user_flag': user_flag,
        })

    @staticmethod
    def get_objects(user, data):
        """

        :param user:
        :param data:
        :return:
        """
        if 'courses' == data:
            objects = Course.objects.filter(user=user)
        elif 'videos' == data:
            objects = Video.objects.filter(user=user)
        else:
            objects = []
        return objects


class CustomBackend(ModelBackend):
    """
    增加邮箱登录
    继承ModelBackend类，覆盖authenticate方法, 增加邮箱认证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 使用get是因为不希望用户存在两个, Q：使用并集查询
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            # 判断密码是否匹配时，django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有check_password(self, raw_password)方法
            if user.check_password(password):
                return user
        except BaseException as e:
            return None


class UserLoginView(View):
    """
    登录
    """
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            user_email = request.POST.get('email', None)
            password = request.POST.get('password', None)
            print(user_email, password)
            # 成功返回user对象，反之返回None, 这里在前面已经增加邮箱登录，所以可以直接把当作username进行登录。
            user = authenticate(username=user_email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                # 如果登录成功，则重定向到个人主页
                return HttpResponseRedirect(reverse('users:user_profile', args=[user.id]))
            else:
                return render(request, 'login.html', {
                    'msg': '邮箱或密码出错',
                    'user_login_form': user_login_form})
        else:
            invalid_keys = [key for key in user_login_form.errors]
            return render(request, 'login.html', {
                'user_login_form': user_login_form,
                'invalid_keys': invalid_keys})


class UserLogoutView(View):
    """
    退出登录
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class UserRegisterView(View):
    """
    注册
    """
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        user_register_form = UserRegisterForm(request.POST)
        print(user_register_form)
        if user_register_form.is_valid():
            user_email = request.POST.get('email', None)
            password1 = request.POST.get('password1', None)
            password2 = request.POST.get('password2', None)
            username = user_email.split('@')[0]

            if not password1 == password2:
                return render(request, 'register.html', {'msg': '密码不一致'})
            if UserProfile.objects.filter(username=username):
                return render(request, 'register.html', {'msg': '用户已存在'})
            # 实例化一个UserProfile对象，并进行相应的赋值
            new_user = UserProfile(username=username, email=user_email)
            # 对保存到数据库的密码加密
            new_user.password = make_password(password1)
            new_user.save()
            return render(request, 'register.html', {'status': 'ok'})
        else:
            invalid_keys = [key for key in user_register_form.errors]
            return render(request, 'register.html', {
                'user_register_form': user_register_form,
                'invalid_keys': invalid_keys,
            })