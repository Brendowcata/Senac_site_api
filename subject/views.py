from rest_framework import viewsets
from .models import SubjectModel
from .serializers import SubjectSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    """Showing all subjects / Exibindo todos os assuntos"""
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    ordering_fields = ['name']
    search_fields = ['name']
