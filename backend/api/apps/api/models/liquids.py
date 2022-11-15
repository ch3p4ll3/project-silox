from django.db import models


class Liquids(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    density = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Liquids"
