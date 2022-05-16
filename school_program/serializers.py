from rest_framework import serializers
from .models import School_ProgramModel
from course.serializers import CourseSerializer

class School_ProgramSerializer(serializers.ModelSerializer):
    class Meta: 
        model = School_ProgramModel
        fields = (
            'id',
            'phase',
            'description',
            'courses',
            )