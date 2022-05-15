from rest_framework import viewsets

from school_program.serializers import School_ProgramSerializer
from .models import School_ProgramModel

class School_ProgramViewSet(viewsets.ModelViewSet):
    """Showing all phases / Exibindo todas as fases"""
    queryset = School_ProgramModel.objects.all()
    serializer_class = School_ProgramSerializer

