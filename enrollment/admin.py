from django.contrib import admin

from enrollment.models import EnrollmentModel

class ListEnrollment(admin.ModelAdmin):
    list_display = ('title_enrollment', 'date_initial', 'date_final', 'courses', 'universities',)
    list_display_links = ('title_enrollment', 'date_initial', 'date_final',)
    search_fields = ('title_enrollment', 'courses', 'universities',)
    list_per_page = 10

admin.site.register(EnrollmentModel, ListEnrollment)
