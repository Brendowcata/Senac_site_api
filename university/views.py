from rest_framework import viewsets, generics
from university.models import UniversityModel
from university.serializers import UniversitySerializer


class UniversityViewSet(viewsets.ModelViewSet):
    """Showing all universities / Exibindo todas as universidades"""
    queryset = UniversityModel.objects.all()
    serializer_class = UniversitySerializer
    http_method_names = ['get', 'post', 'put', 'patch']


