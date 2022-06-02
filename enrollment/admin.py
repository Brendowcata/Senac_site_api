from django.contrib import admin

from enrollment.models import EnrollmentModel

class ListEnrollment(admin.ModelAdmin):
    list_display = ('title_enrollment', 'date_initial', 'date_final', 'courses', 'universities',)
    list_display_links = ('title_enrollment',)
    search_fields = ('title_enrollment', 'courses', 'universities',)
    list_filter = ('date_initial', 'date_final', 'courses', 'universities',)
    ordering = ('title_enrollment',)
    list_per_page = 25

admin.site.register(EnrollmentModel, ListEnrollment)
