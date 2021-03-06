from rest_framework import serializers
from course.validators import *
from .models import CourseModel
from enrollment.serializers import EnrollmentSerializer
from school_program.serializers import School_ProgramSerializer

class CourseSerializer(serializers.ModelSerializer):
    enrollments = EnrollmentSerializer(many = True, read_only=True)
    school_programs = School_ProgramSerializer(many=True, read_only=True)

    class Meta:
        model = CourseModel
        fields = [
            'id',
            'name',
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
            'enrollments',
            'school_programs'
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


class ListCoursesInUniversitySerializer(serializers.ModelSerializer):
    enrollments = EnrollmentSerializer(many = True, read_only=True)
    school_programs = School_ProgramSerializer(many=True, read_only=True)

    class Meta:
        model = CourseModel
        fields = [
            'id',
            'name',
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
            'enrollments',
            'school_programs'
        ]

class ListCoursesInEnrollmentSerializer(serializers.ModelSerializer):
    enrollments = EnrollmentSerializer(many = True, read_only=True)
    school_programs = School_ProgramSerializer(many=True, read_only=True)

    class Meta:
        model = CourseModel
        fields = [
            'id',
            'name',
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
            'enrollments',
            'school_programs'
        ]