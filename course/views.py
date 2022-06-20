from rest_framework import viewsets, generics
from course.models import CourseModel
from course.serializers import CourseSerializer, List_Courses_In_UniversitySerializer

class CourseViewSet(viewsets.ModelViewSet):
    """Showing all courses / Exibindo todos os cursos"""
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    ordering_fields = ['name']
    search_fields = ['name']
    filter_fields = ['course_type', 'occupation_area', 'modality', 'mec_score', 'is_activate']


class List_Courses_In_University(generics.ListAPIView):
    """List all courses at a university / Lista todos os cursos em uma universidade"""
    def get_queryset(self):
        queryset = CourseModel.objects.filter(universitymodel=self.kwargs['pk'])
        return queryset
    serializer_class = List_Courses_In_UniversitySerializer
    ordering_fields = ['name']
    search_fields = ['name']
    filter_fields = ['course_type', 'occupation_area', 'modality', 'mec_score', 'is_activate']