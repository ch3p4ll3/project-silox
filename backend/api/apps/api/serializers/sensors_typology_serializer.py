from rest_framework import serializers
from ..models import SensorsTypology


class SensorsTypologySerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorsTypology
        fields = '__all__'
