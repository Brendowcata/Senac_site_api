from rest_framework import viewsets
from course.models import CourseModel
from university.models import UniversityModel
from university.serializers import UniversityCourseSerializer, UniversitySerializer

class UniversityViewSet(viewsets.ModelViewSet):
    """Showing all universities / Exibindo todas as universidades"""
    queryset = UniversityModel.objects.all()
    serializer_class = UniversitySerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    search_fields = ['name']
    ordering_fields = ['name']
    filter_fields = ['city', 'state', 'is_activate']
    
    def get_serializer_class(self):

        if self.request.method in ['GET']:
            return UniversityCourseSerializer
        return UniversitySerializer







