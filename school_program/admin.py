from django.contrib import admin

from school_program.models import School_ProgramModel

class ListSchool_Program(admin.ModelAdmin):
    list_display = ('phase', 'description', 'courses',)
    list_display_links = ('phase',)
    search_fields = ('phase', 'courses',)
    list_per_page = 10

admin.site.register(School_ProgramModel, ListSchool_Program)

