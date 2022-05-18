from rest_framework import serializers

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
            'courses',
            )

class School_ProgramCourseSubjectSerializer(School_ProgramSerializer):
    courses = CourseSerializer(read_only=True)
    subjects = SubjectSerializer(many=True, read_only=True)