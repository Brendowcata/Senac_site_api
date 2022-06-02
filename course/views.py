from rest_framework import viewsets
from course.models import CourseModel
from course.serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """Showing all courses / Exibindo todos os cursos"""
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    #filterset_fields = ['is_activate']
