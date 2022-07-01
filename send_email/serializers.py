from rest_framework import serializers

from send_email.validators import *
from .models import Send_EmailModel

class Send_EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Send_EmailModel
        fields = [
            'name',
            'email',
            'email_university',
            'phone_number',
            'message',
            'courses',
            'universities'
        ]
    
    def validate(self, data):
        if not name_isValid(data['name']):
            raise serializers.ValidationError(
                {'Name': "Este campo não deve conter números!"}
            )

        if not phone_number_isValid(data['phone_number']):
            raise serializers.ValidationError(
                {'Phone_number': "Este campo deve ter 15 dígitos! Favor utilizar este formato (XX) 9XXXX-XXXX"}
                )

        return data
