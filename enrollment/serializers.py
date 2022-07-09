from rest_framework import serializers

from enrollment.validators import *
from .models import EnrollmentModel

class EnrollmentSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = EnrollmentModel
        fields = (
            'id',
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
    
class ListUniversityCourseEnrollmentSerializer(EnrollmentSerializer):
    universities = serializers.ReadOnlyField(source='universities.name')
    courses = serializers.ReadOnlyField(source='courses.name')

class ListEnrollmentsCourseSerializer(serializers.ModelSerializer):
    universities = serializers.ReadOnlyField(source='universities.name')
    courses = serializers.ReadOnlyField(source='courses.name')

    class Meta:
        model = EnrollmentModel
        fields = (
            'id',
            'date_initial',
            'date_final',
            'courses',
            'universities'
        )

class ListEnrollmentsUniversitySerializer(serializers.ModelSerializer):
    universities = serializers.ReadOnlyField(source='universities.name')
    courses = serializers.ReadOnlyField(source='courses.name')

    class Meta:
        model = EnrollmentModel
        fields = (
            'id',
            'date_initial',
            'date_final',
            'courses',
            'universities'
        )

