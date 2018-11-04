from django.conf import settings
from django.db import models
from django.urls import reverse

from courses.models import Course


class Video(models.Model):
    """
    视频表
    """
    name = models.CharField(max_length=128)
    url = models.URLField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='videos', blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='videos', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('videos:video_detail', args=[self.id])

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return self.name



