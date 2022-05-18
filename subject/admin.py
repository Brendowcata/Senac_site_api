from django.contrib import admin

from subject.models import SubjectModel

class ListSubject(admin.ModelAdmin):
    list_display = ('name', 'subject_time', 'description',)
    list_display_links = ('name',)
    search_fields = ('name', 'subject_time',)
    list_per_page = 10

admin.site.register(SubjectModel, ListSubject)