from django.db import models


class Properties(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Properties"
