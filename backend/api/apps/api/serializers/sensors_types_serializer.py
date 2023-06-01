from rest_framework import serializers
from ..models import SensorsTypes


class SensorsTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorsTypes
        fields = '__all__'
