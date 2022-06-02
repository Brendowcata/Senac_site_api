from rest_framework import viewsets, generics
from course.models import CourseModel
from course.serializers import CourseSerializer, ListCourseUniversitySerializer

class CourseViewSet(viewsets.ModelViewSet):
    """Showing all courses / Exibindo todos os cursos"""
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    ordering_fields = ['name']
    search_fields = ['name']
    filter_fields = ['course_type', 'occupation_area', 'modality', 'mec_score', 'is_activate']


class ListCourseUniversity(generics.ListAPIView):
    
    def get_queryset(self):
        queryset = CourseModel.objects.filter(universitymodel=self.kwargs['pk'])
        return queryset
    serializer_class = ListCourseUniversitySerializer