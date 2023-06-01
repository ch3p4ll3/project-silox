from rest_framework import serializers
from ..models import LiquidProperties


class LiquidsPropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiquidProperties
        fields = '__all__'
