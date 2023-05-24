from rest_framework import serializers
from ..models import Liquids
from ..models import LiquidProperties
from .liquids_properties_serializer import LiquidsPropertiesSerializer


class LiquidsSerializer(serializers.ModelSerializer):
    properties = LiquidsPropertiesSerializer(many=True, required=False)

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

    # edit patch method
    def partial_update(self, instance: Liquids, validated_data):
        properties = validated_data.get("properties")

        if properties is not None:
            properties = []

            for property in validated_data.pop("properties", []):
                obj, _ = LiquidProperties.objects.update_or_create(**property)
                obj.save()
                properties.append(obj)

            instance.properties.set(properties)

        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        return instance

    def update(self, instance: Liquids, validated_data):
        properties = validated_data.get("properties")

        if properties is not None:
            properties = []

            for property in validated_data.pop("properties", []):
                obj, _ = LiquidProperties.objects.update_or_create(**property)
                obj.save()
                properties.append(obj)

            instance.properties.set(properties)

        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        return instance

    class Meta:
        model = Liquids
        fields = '__all__'
        depth = 2
