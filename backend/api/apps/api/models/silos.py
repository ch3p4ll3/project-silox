from django.db import models
from .liquids import Liquids
from .sizes import Sizes
from .sensors_types import SensorsTypes


class Silos(models.Model):
    name = models.CharField(max_length=255)
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE, null=True, blank=True)
    liquid = models.ForeignKey(Liquids, on_delete=models.CASCADE, null=True, blank=True)

    sensors = models.ManyToManyField(SensorsTypes, through='SensorsInSilos')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Silos"
