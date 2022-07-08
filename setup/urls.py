from email.mime import base
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from course.views import CourseViewSet, ListCoursesInEnrollment, ListCoursesInUniversity
from enrollment.views import EnrollmentViewSet, ListEnrollmentsInCourse, ListEnrollmentsInUniversity
from school_program.views import ListSchool_ProgramsInCourse, ListSchool_ProgramsInSubject, School_ProgramViewSet
from subject.views import ListSubjectsInSchool_Program, SubjectViewSet
from university.views import UniversityViewSet, ListUniversitiesInCourse
from send_email.views import Send_EmailViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Senac Site API",
      default_version='v1',
      description="API para gerenciamento de cursos nas universidades Senac SC",
      terms_of_service="#",
      contact=openapi.Contact(email="brendowcata1@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('university', UniversityViewSet, basename='University')
router.register('course', CourseViewSet, basename="Course")
router.register('school_program', School_ProgramViewSet, basename="School_Program")
router.register('subject', SubjectViewSet, basename='Subject')
router.register('enrollment', EnrollmentViewSet, basename='Enrollment')
router.register('send_email', Send_EmailViewSet, basename='Send_Email')


urlpatterns = [
    path('senac-admin/', admin.site.urls),
    path('', include(router.urls)),
    path('rest-auth-token/', obtain_auth_token, name="Token"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('course/<uuid:pk>/enrollments/', ListEnrollmentsInCourse.as_view()),
    path('course/<uuid:pk>/school_programs/', ListSchool_ProgramsInCourse.as_view()),
    path('course/<uuid:pk>/universities/', ListUniversitiesInCourse.as_view()),
    path('university/<uuid:pk>/courses/', ListCoursesInUniversity.as_view()),
    path('university/<uuid:pk>/enrollments/', ListEnrollmentsInUniversity.as_view()),
    path('school_program/<uuid:pk>/subjects/', ListSubjectsInSchool_Program.as_view()),
    path('subject/<uuid:pk>/school_programs/', ListSchool_ProgramsInSubject.as_view()),
    path('enrollment/<uuid:pk>/courses/', ListCoursesInEnrollment.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

