from rest_framework.authentication import TokenAuthentication
from ..models import LiquidProperties

from rest_framework import viewsets

from ..serializers.liquids_properties_serializer import LiquidsPropertiesSerializer
from ..serializers.liquids_properties_serializer_get import LiquidsPropertiesSerializerGet


class LiquidsPropertiesViewSet(viewsets.ModelViewSet):
    queryset = LiquidProperties.objects.all()
    serializer_class = LiquidsPropertiesSerializer
    authentication_classes = (TokenAuthentication,)

    def get_serializer_class(self):
        if self.request and self.request.method != 'GET':
            return LiquidsPropertiesSerializer
        return LiquidsPropertiesSerializerGet
