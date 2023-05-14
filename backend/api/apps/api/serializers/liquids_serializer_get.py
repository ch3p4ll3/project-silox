from rest_framework import serializers
from ..models import Liquids
from ..models import LiquidProperties
from .liquids_properties_serializer_get import LiquidsPropertiesSerializerGet


class LiquidsSerializerGet(serializers.ModelSerializer):
    properties = LiquidsPropertiesSerializerGet(many=True, required=False)

    def create(self, validated_data: dict):
        liquid_properties = validated_data.pop("properties", [])

        liquid_model = Liquids(**validated_data)
        liquid_model.save()

        for liquid_property in liquid_properties:
            prop, _ = LiquidProperties.objects.get_or_create(**liquid_property)
            prop.save()

            liquid_model.properties.add(prop)

        liquid_model.save()

        return liquid_model

    class Meta:
        model = Liquids
        fields = '__all__'
        depth = 2
