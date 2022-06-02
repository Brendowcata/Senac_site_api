from rest_framework import viewsets
from school_program.serializers import School_ProgramCourseSubjectSerializer, School_ProgramSerializer
from .models import School_ProgramModel

class School_ProgramViewSet(viewsets.ModelViewSet):
    """Showing all phases / Exibindo todas as fases"""
    queryset = School_ProgramModel.objects.all()
    serializer_class = School_ProgramSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    def get_serializer_class(self):

        if self.request.method in ['GET']:
            return School_ProgramCourseSubjectSerializer
        return School_ProgramSerializer