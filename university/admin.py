from django.contrib import admin

from university.models import UniversityModel

class ListUniversity(admin.ModelAdmin):
    list_display = ('name', 'telephone', 'phone_number', 'street', 'state',)
    list_display_links = ('name',)
    search_fields = ('name', 'telephone', 'phone_number', 'state',)
    list_per_page = 10

admin.site.register(UniversityModel, ListUniversity)
