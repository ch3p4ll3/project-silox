from django.db import models


class Actions(models.Model):
    action = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    time = models.DateTimeField()

    def __str__(self):
        return self.action

    class Meta:
        verbose_name_plural = "Actions"
