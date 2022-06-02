from django.contrib import admin

from school_program.models import School_ProgramModel

class ListSchool_Program(admin.ModelAdmin):
    list_display = ('phase', 'phase_time', 'courses',)
    list_display_links = ('phase',)
    search_fields = ('phase', 'courses',)
    list_filter = ('phase', 'phase_time', 'courses',)
    ordering = ('courses',)
    list_per_page = 25

admin.site.register(School_ProgramModel, ListSchool_Program)

