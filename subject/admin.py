from django.contrib import admin

from subject.models import SubjectModel

class ListSubject(admin.ModelAdmin):
    list_display = ('name', 'description',)
    list_display_links = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 25

admin.site.register(SubjectModel, ListSubject)