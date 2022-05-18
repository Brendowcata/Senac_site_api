from rest_framework import serializers
from .models import CourseModel

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = (
            'id',
            'name',
            'banner',
            'description',
            'course_type',
            'course_objective',
            'curriculum',
            'completion_profile',
            'duration_time',
            'occupation_area',
            'is_activate',
            'modality',
            'value',
            'enrollment')