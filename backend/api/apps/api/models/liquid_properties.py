from django.db import models
from .property import Properties


class LiquidProperties(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    min = models.FloatField()
    max = models.FloatField()

    def __str__(self):
        return f"{self.property.name} ({self.min} - {self.max})"

    class Meta:
        verbose_name_plural = "Liquid Properties"
