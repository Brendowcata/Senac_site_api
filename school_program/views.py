from rest_framework import viewsets, generics
from school_program.serializers import List_School_Programs_In_CourseSerializer, List_School_Programs_In_SubjectSerializer, School_ProgramSubjectSerializer, School_ProgramSerializer
from .models import School_ProgramModel

class School_ProgramViewSet(viewsets.ModelViewSet):
    """Showing all phases / Exibindo todas as fases"""
    queryset = School_ProgramModel.objects.all()
    serializer_class = School_ProgramSerializer
    ordering_fields = ['courses']
    search_fields = ['subjects']
    filter_fields = ['phase', 'phase_time', 'courses']

    def get_serializer_class(self):

        if self.request.method in ['GET']:
            return School_ProgramSubjectSerializer
        return School_ProgramSerializer

class List_School_Programs_In_Course(generics.ListAPIView):
    """Lists all phases of a course / Lista todas as fases de um curso"""
    def get_queryset(self):
        queryset = School_ProgramModel.objects.filter(courses_id=self.kwargs['pk'])
        return queryset
    serializer_class = List_School_Programs_In_CourseSerializer
    ordering_fields = ['courses']
    search_fields = ['subjects']
    filter_fields = ['phase', 'phase_time', 'courses']

class List_School_Programs_In_Subject(generics.ListAPIView):
    """Lists all phases that contain the subject / Lista todas as fases que contêm o assunto"""
    def get_queryset(self):
        queryset = School_ProgramModel.objects.filter(subjects=self.kwargs['pk'])
        return queryset
    serializer_class = List_School_Programs_In_SubjectSerializer
    ordering_fields = ['courses']
    search_fields = ['subjects']
    filter_fields = ['phase', 'phase_time', 'courses']
    