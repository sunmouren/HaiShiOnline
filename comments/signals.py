# encoding: utf-8
"""
@author: Sunmouren
@contact: sunxuechao1024@gmail.com
@time: 2018/11/3 18:43
@desc: 及时更新点赞人数
"""

from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import Comment


@receiver(m2m_changed, sender=Comment.like_user.through)
def like_user_changed(sender, instance, **kwargs):
    instance.like_number = instance.like_user.count()
    instance.save()
