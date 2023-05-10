from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Liquids(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, null=True, blank=True)
    density = models.FloatField()
    pHMin = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0), MaxValueValidator(13.0)])
    pHMax = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0), MaxValueValidator(13)])
    cO2Min = models.FloatField(null=True, blank=True, help_text="% CO2")
    cO2Max = models.FloatField(null=True, blank=True, help_text="% CO2")
    tempMin = models.FloatField(null=True, blank=True, help_text="°C")
    tempMax = models.FloatField(null=True, blank=True, help_text="°C")
    maxPression = models.FloatField(null=True, blank=True)
    minPression = models.FloatField(null=True, blank=True, default=1.0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Liquids"
