from rest_framework import serializers
from .models import SubjectModel

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectModel
        fields = (
            'id',
            'name',
            'description',
            )