from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.decorators import action

from ..models.logs import Logs
from ..models.silos import Silos
from ..serializers.logs_serializer import LogsSerializer


class LogsViewSet(viewsets.ModelViewSet):
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer
    http_method_names = ('get',)
    authentication_classes = (TokenAuthentication,)

    @action(url_path=r'(?P<silos_id>\w+)/last/(?P<logs_number>\w+)', detail=False)
    def last_silos_log(self, request, silos_id, logs_number):
        try:
            silos = Silos.objects.get(id=silos_id)
        except Silos.DoesNotExist:
            return Response({"detail": "Silos not found"}, status=HTTP_404_NOT_FOUND)

        last_log = Logs.get_by_silos(silos, int(logs_number))
        return Response(LogsSerializer(last_log, many=True).data)
