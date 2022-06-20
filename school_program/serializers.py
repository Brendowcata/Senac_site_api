from rest_framework import serializers
from school_program.validators import *

from subject.serializers import SubjectSerializer
from .models import School_ProgramModel
from course.serializers import CourseSerializer

class School_ProgramSerializer(serializers.ModelSerializer):
    courses = serializers.ReadOnlyField(source='courses.name')

    class Meta: 
        model = School_ProgramModel
        fields = [
            'id',
            'phase',
            'phase_time',
            'courses',
            'subjects',
            ]

    def validate(self, data):
        if not phase_time_isValid(data['phase_time']):
            raise serializers.ValidationError(
                {'Phase_time': "O tempo de duração da fase deve ser maior que 0"}
            )

        if not phase_isValid(data['phase']):
            raise serializers.ValidationError(
                {'Phase': "A fase deve ser maior que 0"}
            )
        return data

class School_ProgramSubjectSerializer(School_ProgramSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)


class List_School_Programs_In_CourseSerializer(serializers.ModelSerializer):
    courses = serializers.ReadOnlyField(source='courses.name')
    subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = School_ProgramModel
        fields = [
            'phase',
            'phase_time',
            'courses',
            'subjects',
            ]

class List_School_Programs_In_SubjectSerializer(serializers.ModelSerializer):
    courses = serializers.ReadOnlyField(source='courses.name')
    subjects = SubjectSerializer(many=True, read_only=True)
    
    class Meta:
        model = School_ProgramModel
        fields = [
            'phase',
            'phase_time',
            'courses',
            'subjects',
            ]
