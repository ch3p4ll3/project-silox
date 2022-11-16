from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from ..utils.influx_management import InfluxDb
from ..api.models.silos import Silos


class EmqxWebhoox(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        data = request.data

        heigth = Silos.objects.filter(id=data['id']).first().height
        InfluxDb().write(data, heigth)  # salvataggio dati su influx
        # TODO: modifica altezza sensori con (altezza silos - valore)
        return Response()
