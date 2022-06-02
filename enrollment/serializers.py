from rest_framework import serializers

from course.serializers import CourseSerializer
from enrollment.validators import *
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
    
    def validate(self, data):
        if not date_initial_smaller_date_final(data['date_initial'], data['date_final']):
            raise serializers.ValidationError(
                {'Date': "O Tempo inicial deve ser menor que o tempo final!"}
            )
        return data

class EnrollmentCourseUniversitySerializer(EnrollmentSerializer):
    courses = CourseSerializer(read_only=True)
    universities = UniversitySerializer(read_only=True)