from django.db import models


class SensorsTypes(models.Model):
    sensor_name = models.CharField(max_length=255)
    sensor_type = models.CharField(max_length=255)
    sensor_slug = models.CharField(max_length=255)
    maintenance_interval = models.IntegerField(help_text="days")
    min_value = models.FloatField(help_text="(SI)")
    max_value = models.FloatField(help_text="(SI)")

    def __str__(self):
        return f"{self.sensor_name}"

    class Meta:
        verbose_name_plural = "Sensors Types"
