from django.contrib import admin

from course.models import CourseModel

class ListCourse(admin.ModelAdmin):
    list_display = ('name', 'description', 'course_type', 'duration_time', 'occupation_area', 'modality', 'is_activate',)
    list_display_links = ('name',)
    search_fields = ('name', 'course_type', 'occupation_area', 'modality',)
    list_filter = ('course_type', 'occupation_area', 'modality', 'is_activate',)
    list_editable = ('is_activate',)
    ordering = ('name',)
    list_per_page =  25
admin.site.register(CourseModel, ListCourse)
