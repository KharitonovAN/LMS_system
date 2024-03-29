from django.contrib import admin
from main_app.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description',)
    list_filter = ('title',)
    search_fields = ('title', 'description',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'course', 'video_url', 'course')
    search_fields = ('course',)
