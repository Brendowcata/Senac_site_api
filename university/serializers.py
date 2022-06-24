from rest_framework import serializers
from course.serializers import CourseSerializer
from university.validators import *
from .models import UniversityModel

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityModel
        fields = (
            'id',
            'name',
            'telephone',
            'phone_number',
            'attendance',
            'email',
            'street',
            'neighborhood',
            'city',
            'state',
            'zip_code',
            'house_number',
            'university_image_local',
            'is_activate',
            'courses',)

    def validate(self, data):
        if not telephone_isValid(data['telephone']):
            raise serializers.ValidationError(
                {'Telephone': "Este campo deve ter 14 dígitos! Favor utilizar este formato (XX) XXXX-XXXX"}
                )
        
        if not name_isValid(data['name']):
            raise serializers.ValidationError(
                {'Name': "Este campo não deve conter números!"}
            )

        if not city_isValid(data['city']):
            raise serializers.ValidationError(
                {'City': "Este campo não deve conter números!"}
            )
        
        if not phone_number_isValid(data['phone_number']):
            raise serializers.ValidationError(
                {'Phone_number': "Este campo deve ter 15 dígitos! Favor utilizar este formato (XX) 9XXXX-XXXX"}
                )
        
        if not zip_code_isValid(data['zip_code']):
            raise serializers.ValidationError(
                {'Zip_code': "Este campo deve conter 9 dígitos! Favor utilizar este formato XXXXX-XXX"}
            )
        
        if not house_number_isValid(data['house_number']):
            raise serializers.ValidationError(
                {'House_number': "Este campo deve incluir apenas números!"}
            )

        return data

class UniversityCoursesSerializer(UniversitySerializer):
    courses = CourseSerializer(many=True, read_only=True)

class ListUniversitiesInCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityModel
        fields = (
            'id',
            'name',
            'telephone',
            'phone_number',
            'attendance',
            'email',
            'street',
            'neighborhood',
            'city',
            'state',
            'zip_code',
            'house_number',
            'university_image_local',
            'is_activate',
            'courses',)

        





        