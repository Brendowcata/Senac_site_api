from rest_framework import serializers
from .models import UniversityModel
from course.serializers import CourseSerializer

class UniversitySerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = UniversityModel
        fields = (
            'id',
            'name',
            'telephone',
            'phone_number',
            'email',
            'street',
            'neighborhood',
            'city',
            'state',
            'zip_code',
            'house_number',
            'courses',)