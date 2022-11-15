from rest_framework import serializers
from ..models.actions import Actions


class ActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actions
        fields = ('id', 'action', 'description', 'time')
