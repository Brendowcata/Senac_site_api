"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from email.mime import base
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from course.views import CourseViewSet, ListCoursesInUniversity
from enrollment.views import EnrollmentViewSet, ListEnrollmentCourse
from school_program.views import ListSchool_ProgramsInCourse, ListSchool_ProgramsInSubject, School_ProgramViewSet
from subject.views import ListSubjectsInSchool_Program, SubjectViewSet
from university.views import UniversityViewSet

router = routers.DefaultRouter()
router.register('university', UniversityViewSet, basename='University')
router.register('course', CourseViewSet, basename="Course")
router.register('school_program', School_ProgramViewSet, basename="School_Program")
router.register('subject', SubjectViewSet, basename='Subject')
router.register('enrollment', EnrollmentViewSet, basename='Enrollment')

urlpatterns = [
    path('senac-admin/', admin.site.urls),
    path('login/', obtain_auth_token, name="obtain-auth-token"),
    path('', include(router.urls)),
    path('course/<uuid:pk>/enrollments/', ListEnrollmentCourse.as_view()),
    path('course/<uuid:pk>/school_programs/', ListSchool_ProgramsInCourse.as_view()),
    path('university/<uuid:pk>/courses/', ListCoursesInUniversity.as_view()),
    path('school_program/<uuid:pk>/subjects/', ListSubjectsInSchool_Program.as_view()),
    path('subject/<uuid:pk>/school_programs/', ListSchool_ProgramsInSubject.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
