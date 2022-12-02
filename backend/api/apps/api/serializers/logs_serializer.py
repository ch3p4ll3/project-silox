from rest_framework import serializers
from ..models.logs import Logs


class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = ('id', 'status', 'description', 'silos', 'time')
