from django.db import models


class Liquids(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, null=True, blank=True)
    density = models.FloatField()
    pHMin = models.FloatField(null=True, blank=True)
    pHMax = models.FloatField(null=True, blank=True)
    cO2Min = models.FloatField(null=True, blank=True)
    cO2Max = models.FloatField(null=True, blank=True)
    tempMin = models.FloatField(null=True, blank=True)
    tempMax = models.FloatField(null=True, blank=True)
    maxPression = models.FloatField(null=True, blank=True)
    minPression = models.FloatField(null=True, blank=True, default=1.0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Liquids"
