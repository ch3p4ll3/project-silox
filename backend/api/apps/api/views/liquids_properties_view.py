from rest_framework.authentication import TokenAuthentication
from ..models import LiquidProperties

from rest_framework import viewsets

from ..serializers.liquids_properties_serializer import LiquidsPropertiesSerializer


class LiquidsPropertiesViewSet(viewsets.ModelViewSet):
    queryset = LiquidProperties.objects.all()
    serializer_class = LiquidsPropertiesSerializer
    authentication_classes = (TokenAuthentication,)
