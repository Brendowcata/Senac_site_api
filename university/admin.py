from django.contrib import admin

from university.models import UniversityModel

class ListUniversity(admin.ModelAdmin):
    list_display = ('name', 'email', 'telephone', 'phone_number', 'street', 'state', 'is_activate')
    list_display_links = ('name',)
    search_fields = ('name', 'telephone', 'phone_number', 'state',)
    list_filter = ('state', 'city', 'is_activate',)
    list_editable = ('is_activate',)
    ordering = ('name',)
    list_per_page = 25

admin.site.register(UniversityModel, ListUniversity)
