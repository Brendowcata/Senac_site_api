from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from course.views import CourseViewSet, ListCoursesInUniversity
from enrollment.views import EnrollmentViewSet, List_Enrollments_In_Course
from school_program.views import List_School_Programs_In_Course, List_School_Programs_In_Subject, School_ProgramViewSet
from subject.views import List_Subjects_In_School_Program, SubjectViewSet
from university.views import UniversityViewSet, ListUniversitiesInCourse

schema_view = get_schema_view(
   openapi.Info(
      title="Senac Site API",
      default_version='v1',
      description="API para gerenciamento de cursos na universidade Senac SC",
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



urlpatterns = [
    path('senac-admin/', admin.site.urls),
    path('', include(router.urls)),
    path('rest-auth-token/', obtain_auth_token, name="Token"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('course/<uuid:pk>/enrollments/', List_Enrollments_In_Course.as_view()),
    path('course/<uuid:pk>/school_programs/', List_School_Programs_In_Course.as_view()),
    path('course/<uuid:pk>/universities/', ListUniversitiesInCourse.as_view()),
    path('university/<uuid:pk>/courses/', ListCoursesInUniversity.as_view()),
    path('school_program/<uuid:pk>/subjects/', List_Subjects_In_School_Program.as_view()),
    path('subject/<uuid:pk>/school_programs/', List_School_Programs_In_Subject.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

