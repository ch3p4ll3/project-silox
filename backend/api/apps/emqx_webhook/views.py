from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from ..utils.influx_management import InfluxDb
from ..api.models.silos import Silos


class EmqxWebhoox(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        data = request.data
        height = Silos.objects.get(id=data['id']).size.height
        InfluxDb().write(data, height)  # salvataggio dati su influx
        return Response()
