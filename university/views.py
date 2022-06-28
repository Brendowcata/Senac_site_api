from rest_framework import viewsets, generics
from university.models import UniversityModel
from university.serializers import UniversityCoursesSerializer, UniversitySerializer, ListUniversitiesInCourseSerializer

class UniversityViewSet(viewsets.ModelViewSet):
    """Showing all universities / Exibindo todas as universidades"""
    queryset = UniversityModel.objects.all()
    serializer_class = UniversitySerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    search_fields = ['name']
    ordering_fields = ['name']
    filterset_fields = ['city', 'state', 'is_activate']

    def get_serializer_class(self):

        if self.request.method in ['GET']:
            return UniversityCoursesSerializer
        return UniversitySerializer

class ListUniversitiesInCourse(generics.ListAPIView):
    """List all universities at a course / Lista todas universidades em um curso"""
    def get_queryset(self):
        queryset = UniversityModel.objects.filter(courses=self.kwargs['pk'])
        return queryset
    serializer_class = ListUniversitiesInCourseSerializer
    search_fields = ['name']
    ordering_fields = ['name']
    filterset_fields = ['city', 'state', 'is_activate']
    
    





