from django.contrib import admin

from course.models import CourseModel

class ListCourse(admin.ModelAdmin):
    list_display = ('name', 'description', 'course_type', 'duration_time', 'occupation_area', 'modality')
    list_display_links = ('name', 'course_type', 'occupation_area', 'modality',)
    search_fields = ('name', 'course_type', 'occupation_area', 'modality',)
    list_per_page = 10

admin.site.register(CourseModel, ListCourse)
