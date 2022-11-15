from django.db import models


class Zones(models.Model):
    name = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Zone"
