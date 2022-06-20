from rest_framework import serializers
from course.validators import *
from .models import CourseModel

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseModel
        fields = [
            'id',
            'name',
            'description',
            'course_type',
            'course_objective',
            'curriculum',
            'completion_profile',
            'duration_time',
            'occupation_area',
            'course_image',
            'is_activate',
            'modality',
            'mec_score',
            ]

    def validate(self, data):
        if not duration_time_isValid(data['duration_time']):
           raise serializers.ValidationError(
               {'Duration_time': "O tempo de duração do curso deve ser maior que 0!"}
           )
        
        if not name_isValid(data['name']):
            raise serializers.ValidationError(
                {'Name': "Este campo não deve conter números!"}
            )

        if not occupation_area_isValid(data['occupation_area']):
            raise serializers.ValidationError(
                {'Occupation_area': "Este campo não deve conter números!"}
            )

        return data

class List_Courses_In_UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = [
            'id',
            'name',
            'description',
            'course_type',
            'course_objective',
            'curriculum',
            'completion_profile',
            'duration_time',
            'occupation_area',
            'course_image',
            'is_activate',
            'modality',
            'mec_score',
        ]