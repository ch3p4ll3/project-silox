from django.db import models
from .liquids import Liquids
from ...utils.influx_management import InfluxDb
from django.conf import settings


class Silos(models.Model):
    name = models.CharField(max_length=255)
    height = models.FloatField()
    diameter = models.FloatField()
    liquid = models.ForeignKey(Liquids, on_delete=models.CASCADE)

    def lastmeasurement(self) -> dict:
        data = InfluxDb().read(self, last=True)
        return data

    def is_worker_running(self):
        worker = next((i for i in settings.SIMS if i.silos.id == self.id), None)

        return worker is not None

    def __str__(self):
        return f"silos#{self.id}"

    class Meta:
        verbose_name_plural = "Silos"
