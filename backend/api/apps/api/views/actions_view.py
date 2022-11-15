from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

from ..models.actions import Actions
from ..serializers.actions_serializer import ActionsSerializer


class ActionsViewSet(viewsets.ModelViewSet):
    queryset = Actions.objects.all()
    serializer_class = ActionsSerializer
    http_method_names = ('get', 'post')
    authentication_classes = (TokenAuthentication,)
