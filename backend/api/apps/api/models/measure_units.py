from django.db import models


class MeasureUnits(models.Model):
    unit = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.unit}"

    class Meta:
        verbose_name_plural = "Measure Units"
