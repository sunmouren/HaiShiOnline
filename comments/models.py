from django.conf import settings
from django.db import models

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

from videos.models import Video


class Comment(MPTTModel):
    """
    多级评论表
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='user_comments')
    video = models.ForeignKey(Video, on_delete=models.CASCADE,
                              related_name='video_comments',
                              blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                            related_name='replies')
    content = models.TextField()
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments', blank=True)
    like_number = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class MPTTMeta:
        order_insertion_by = ('-created', )

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.parent is not None:
            return '{0} 回复 {1}'.format(self.user, self.parent.user)
        else:
            return '{0} 评论了 {1}'.format(self.user, self.video)