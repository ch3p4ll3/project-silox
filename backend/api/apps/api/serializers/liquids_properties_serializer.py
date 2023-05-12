from rest_framework import serializers
from ..models import LiquidProperties
from .properties_serializer import PropertiesSerializer


class LiquidsPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiquidProperties
        fields = '__all__'
