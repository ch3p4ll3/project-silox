from django.db import models
from .liquids import Liquids
from .sizes import Sizes
from .sensors_types import SensorsTypes
from ...utils.influx_management import InfluxDb
from django.conf import settings


class Silos(models.Model):
    name = models.CharField(max_length=255)
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE, null=True, blank=True)
    liquid = models.ForeignKey(Liquids, on_delete=models.CASCADE, null=True, blank=True)

    sensors = models.ManyToManyField(SensorsTypes, through='SensorsInSilos')

    def lastmeasurement(self) -> dict:
        data = InfluxDb().read(self, last=True)
        return data

    def is_worker_running(self) -> bool:
        worker = next((i for i in settings.SIMS if i.silos.id == self.id), None)

        return worker is not None

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Silos"
