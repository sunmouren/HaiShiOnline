from django.contrib import admin

from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created']
    list_filter = ['name', 'created']
    search_fields = ['name']