from rest_framework import serializers
from ..models import MeasureUnits


class MeasureUnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnits
        fields = '__all__'
