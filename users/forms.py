# encoding: utf-8
"""
@author: Sunmouren
@contact: sunxuechao1024@gmail.com
@time: 2018/11/4 14:20
@desc: 
"""
from django import forms

from .models import UserProfile


class UserLoginForm(forms.Form):
    """
    登录验证表单
    """
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)

