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

        return data
