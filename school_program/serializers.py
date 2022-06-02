from rest_framework import serializers
from school_program.validators import *

from subject.serializers import SubjectSerializer
from .models import School_ProgramModel
from course.serializers import CourseSerializer

class School_ProgramSerializer(serializers.ModelSerializer):
    class Meta: 
        model = School_ProgramModel
        fields = (
            'id',
            'phase',
            'subjects',
            'phase_time',
            'courses',
            )

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

class School_ProgramCourseSubjectSerializer(School_ProgramSerializer):
    courses = CourseSerializer(read_only=True)
    subjects = SubjectSerializer(many=True, read_only=True)