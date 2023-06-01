from rest_framework.authentication import TokenAuthentication
from ..models import Properties

from rest_framework import viewsets

from ..serializers.properties_serializer import PropertiesSerializer


class PropertiesViewSet(viewsets.ModelViewSet):
    queryset = Properties.objects.all()
    serializer_class = PropertiesSerializer
    authentication_classes = (TokenAuthentication,)
