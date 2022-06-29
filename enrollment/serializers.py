from rest_framework import serializers

from enrollment.validators import *
from .models import EnrollmentModel

class EnrollmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EnrollmentModel
        fields = (
            'id',
            'title_enrollment',
            'date_initial',
            'date_final',
            'courses',
            'universities'
        )
    
    def validate(self, data):
        if not date_initial_smaller_date_final(data['date_initial'], data['date_final']):
            raise serializers.ValidationError(
                {'Date': "O Tempo inicial deve ser menor que o tempo final!"}
            )
        return data
    
    def create(self, validated_data):
        title_enrollment = str(
            validated_data.get('universities')) + ' - ' +str(
            validated_data.get('date_initial')
            .strftime("%d/%m/%Y")) + ' - ' + str(
                validated_data.get('date_final')
                .strftime("%d/%m/%Y"))
        validated_data['title_enrollment'] = title_enrollment
        return super().create(validated_data)
    
    

class ListEnrollmentsCourseSerializer(serializers.ModelSerializer):
    universities = serializers.ReadOnlyField(source='universities.name')

    class Meta:
        model = EnrollmentModel
        fields = [
            'title_enrollment',
            'date_initial',
            'date_final',
            'universities'
        ]

