# encoding: utf-8
"""
@author: Sunmouren
@contact: sunxuechao1024@gmail.com
@time: 2018/11/4 9:52
@desc: 
"""

from django import template


register = template.Library()


@register.simple_tag
def check_is_liked(request, comment):
    """
    检查当前用户是否在喜欢列表里
    :param request:
    :param comment: 评论
    :return: False or True
    """
    return request.user in comment.like_user.all()