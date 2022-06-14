from rest_framework import serializers

from subject.validators import *
from .models import SubjectModel

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectModel
        fields = [
            'id',
            'name',
            'description',
            ]
    
    def validate(self, data):

        if not name_isValid(data['name']):
            raise serializers.ValidationError(
                {'Name': "Este campo não deve conter números!"}
            )

        return data

class ListSubjectsInSchool_ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectModel
        fields = [
            'name',
            'description',
            ]