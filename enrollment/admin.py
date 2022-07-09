from django.contrib import admin

from enrollment.models import EnrollmentModel

class ListEnrollment(admin.ModelAdmin):
    list_display = ('date_initial', 'date_final', 'courses', 'universities',)
    list_display_links = ('date_initial', 'date_final',)
    search_fields = ('courses', 'universities',)
    list_filter = ('date_initial', 'date_final', 'courses', 'universities',)
    ordering = ('courses', 'universities')
    list_per_page = 25

admin.site.register(EnrollmentModel, ListEnrollment)
