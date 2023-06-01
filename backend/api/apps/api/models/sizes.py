from django.db import models


class Sizes(models.Model):
    description = models.CharField(max_length=255)
    height = models.FloatField()
    diameter = models.FloatField()
    tare = models.FloatField()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "Sizes"
