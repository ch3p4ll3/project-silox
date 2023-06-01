from django.db import models
from .silos import Silos
from .sensors_typology import SensorsTypology


class SensorsInSilos(models.Model):
    silos = models.ForeignKey(Silos, on_delete=models.CASCADE)
    sensor = models.ForeignKey(SensorsTypology, on_delete=models.CASCADE)
    last_maintenance = models.DateTimeField()
    position = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.sensor.sensor_name}-{self.silos.id}"

    class Meta:
        verbose_name_plural = "Sensors In Silos"
