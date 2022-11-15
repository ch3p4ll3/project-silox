from django.db import models
from .zones import Zones
from .liquids import Liquids
from .actions import Actions
from ...utils.influx_management import InfluxDb


class Silos(models.Model):
    heigth = models.FloatField()
    diameter = models.FloatField()
    zone = models.ForeignKey(Zones, on_delete=models.CASCADE)
    liquid = models.ForeignKey(Liquids, on_delete=models.CASCADE)
    actions = models.ManyToManyField(Actions, blank=True)

    def lastmeasurement(self) -> dict:
        # prendere ultima misurazione da influx
        data = InfluxDb().read(self.id, last=True)
        return data

    def __str__(self):
        return f"silos#{self.id}"

    class Meta:
        verbose_name_plural = "Silos"
