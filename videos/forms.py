# encoding: utf-8
"""
@author: Sunmouren
@contact: sunxuechao1024@gmail.com
@time: 2018/10/28 23:49
@desc: 
"""

from django import forms

from .models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'course', 'url']


class UserRegisterForm(forms.Form):
    """
    注册验证表单
    """
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)
