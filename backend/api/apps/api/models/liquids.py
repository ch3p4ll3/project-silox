from django.db import models
from .liquid_properties import LiquidProperties


class Liquids(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, null=True, blank=True)
    density = models.FloatField()

    properties = models.ManyToManyField(LiquidProperties, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Liquids"
