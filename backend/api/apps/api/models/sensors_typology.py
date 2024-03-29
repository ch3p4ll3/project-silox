from django.db import models
from .sensors_types import SensorsTypes
from .measure_units import MeasureUnits


class SensorsTypology(models.Model):
    sensor_name = models.CharField(max_length=255)
    sensor_type = models.ForeignKey(SensorsTypes, on_delete=models.CASCADE)
    sensor_slug = models.CharField(max_length=255)
    maintenance_interval = models.IntegerField(help_text="days")
    measure_unit = models.ForeignKey(MeasureUnits, on_delete=models.CASCADE)
    min_value = models.FloatField(help_text="(SI)")
    max_value = models.FloatField(help_text="(SI)")

    def __str__(self):
        return f"{self.sensor_name}"

    class Meta:
        verbose_name_plural = "Sensors Topologies"
