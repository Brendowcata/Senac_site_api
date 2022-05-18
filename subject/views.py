from rest_framework import viewsets
from .models import SubjectModel
from .serializers import SubjectSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
