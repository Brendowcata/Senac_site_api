from rest_framework import serializers

from course.serializers import CourseSerializer
from university.serializers import UniversitySerializer
from .models import EnrollmentModel

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrollmentModel
        fields = (
            'id',
            'title_enrollment',
            'date_initial',
            'date_final',
            'courses',
            'universities'
        )

class EnrollmentCourseUniversitySerializer(EnrollmentSerializer):
    courses = CourseSerializer(read_only=True)
    universities = UniversitySerializer(read_only=True)