from rest_framework import serializers
from ..models import LiquidProperties
from .properties_serializer import PropertiesSerializer


class LiquidsPropertiesSerializer(serializers.ModelSerializer):
    property = PropertiesSerializer()

    class Meta:
        model = LiquidProperties
        fields = ('id', 'property', 'min', 'max')
