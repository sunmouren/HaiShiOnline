from django.db import models


class Video(models.Model):
    """
    视频表
    """
    title = models.CharField(verbose_name='标题', max_length=128)
    url = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return self.title



