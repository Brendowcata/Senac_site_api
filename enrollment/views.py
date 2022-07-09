from rest_framework import viewsets, generics
from enrollment.models import EnrollmentModel
from enrollment.serializers import EnrollmentSerializer, ListEnrollmentsCourseSerializer, ListEnrollmentsUniversitySerializer, ListUniversityCourseEnrollmentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    """Showing all Enrollments / Exibindo todas as inscrições"""
    queryset = EnrollmentModel.objects.all()
    serializer_class = EnrollmentSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    filterset_fields = ['date_initial', 'date_final']

    def get_serializer_class(self):

        if self.request.method in ['GET']:
            return ListUniversityCourseEnrollmentSerializer
        return EnrollmentSerializer

class ListEnrollmentsInCourse(generics.ListAPIView):
    """Lists all enrollments in a course / Lista todas as inscrições em um curso"""
    def get_queryset(self):
        queryset = EnrollmentModel.objects.filter(courses_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListEnrollmentsCourseSerializer
    filterset_fields = ['date_initial', 'date_final']

class ListEnrollmentsInUniversity(generics.ListAPIView):
    """Lists all enrollments in a university / Lista todas as inscrições em uma universidade"""
    def get_queryset(self):
        queryset = EnrollmentModel.objects.filter(universities_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListEnrollmentsUniversitySerializer
    filterset_fields = ['date_initial', 'date_final']
