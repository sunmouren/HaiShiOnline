from django.db import models
from django.conf import settings
from django.urls import reverse


class Course(models.Model):
    """
    课程表
    """
    name = models.CharField(max_length=64)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='courses')
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('courses:course_detail', args=[self.id])

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name
        ordering = ('-created', )

    def __str__(self):
        return self.name
