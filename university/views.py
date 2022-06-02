from rest_framework import viewsets
from university.models import UniversityModel
from university.serializers import UniversityCourseSerializer, UniversitySerializer

class UniversityViewSet(viewsets.ModelViewSet):
    """Showing all universities / Exibindo todas as universidades"""
    queryset = UniversityModel.objects.all()
    serializer_class = UniversitySerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    
    #ordering_fields = ['name', 'city']
    #filter_fields = ['city', 'name', 'state']
    def get_serializer_class(self):

        if self.request.method in ['GET']:
            return UniversityCourseSerializer
        return UniversitySerializer





