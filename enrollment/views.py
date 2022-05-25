from rest_framework import viewsets

from enrollment.models import EnrollmentModel
from enrollment.serializers import EnrollmentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    """Showing all Enrollments / Exibindo todas as inscrições"""
    queryset = EnrollmentModel.objects.all()
    serializer_class = EnrollmentSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
