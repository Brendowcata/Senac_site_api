from rest_framework import serializers
from .models import EnrollmentModel

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrollmentModel
        fields = (
            'id',
            'is_activate',
            'date_initial',
            'date_final'
        )