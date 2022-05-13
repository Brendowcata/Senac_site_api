from rest_framework import views

from school_program.serializers import School_ProgramSerializer
from .models import School_ProgramModel

class School_ProgramViewSet(viewsets.ModelViewSet):
    """Showing all universities / Exibindo todas as universidades"""
    queryset = School_ProgramModel.objects.all()
    serializer_class = School_ProgramSerializer

