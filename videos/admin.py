from django.contrib import admin

from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'url', 'created']
    list_filter = ['title', 'created']
    search_fields = ['title']



