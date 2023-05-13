from rest_framework import serializers
from ..models import LiquidProperties
from .properties_serializer import PropertiesSerializer


class LiquidsPropertiesSerializer(serializers.ModelSerializer):
    property = PropertiesSerializer(read_only=True)

    class Meta:
        model = LiquidProperties
        fields = '__all__'
