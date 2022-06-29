from rest_framework import viewsets, generics
from enrollment.models import EnrollmentModel
from enrollment.serializers import EnrollmentSerializer, ListEnrollmentsCourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    """Showing all Enrollments / Exibindo todas as inscrições"""
    queryset = EnrollmentModel.objects.all()
    serializer_class = EnrollmentSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    ordering_fields = ['title_enrollment']
    search_fields = ['title_enrollment',]
    filterset_fields = ['title_enrollment', 'date_initial', 'date_final']

   

class ListEnrollmentsInCourse(generics.ListAPIView):
    """Lists all enrollments in a course / Lista todas as inscrições em um curso"""
    def get_queryset(self):
        queryset = EnrollmentModel.objects.filter(courses_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListEnrollmentsCourseSerializer
    ordering_fields = ['title_enrollment']
    search_fields = ['title_enrollment',]
    filterset_fields = ['tittle_enrollment', 'date_initial', 'date_final']
