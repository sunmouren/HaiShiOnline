from django.db import models


class Course(models.Model):
    """
    课程表
    """
    name = models.CharField(verbose_name='课程名', max_length=64)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name
        ordering = ('-created', )

    def __str__(self):
        return self.name
