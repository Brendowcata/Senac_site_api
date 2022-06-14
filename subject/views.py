from rest_framework import viewsets, generics
from .models import SubjectModel
from .serializers import ListSubjectsInSchool_ProgramSerializer, SubjectSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    """Showing all subjects / Exibindo todos os assuntos"""
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer
    ordering_fields = ['name']
    search_fields = ['name']

class ListSubjectsInSchool_Program(generics.ListAPIView):

    def get_queryset(self):
        queryset = SubjectModel.objects.filter(school_programmodel=self.kwargs['pk'])
        return queryset
    serializer_class = ListSubjectsInSchool_ProgramSerializer
    ordering_fields = ['name']
    search_fields = ['name']
