from rest_framework import serializers
from .models import UniversityModel

class UniversitySerializer(serializers.ModelSerializer):
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