from django.contrib import admin

from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url', 'created']
    list_filter = ['name', 'created']
    search_fields = ['name']



