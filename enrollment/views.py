from rest_framework import viewsets
from enrollment.models import EnrollmentModel
from enrollment.serializers import EnrollmentCourseUniversitySerializer, EnrollmentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    """Showing all Enrollments / Exibindo todas as inscrições"""
    queryset = EnrollmentModel.objects.all()
    serializer_class = EnrollmentSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    ordering_fields = ['title_enrollment']
    search_fields = ['title_enrollment', 'date_initial', 'date_final']
    filter_fields = ['title_enrollment', 'date_initial', 'date_final', 'courses', 'universities']

    def get_serializer_class(self):
        
        if self.request.method in ['GET']:
            return EnrollmentCourseUniversitySerializer
        return EnrollmentSerializer
