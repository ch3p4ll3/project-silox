from django.db import models
from .silos import Silos


class Logs(models.Model):
    status = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    silos = models.ForeignKey(Silos, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_by_silos(cls, silos: Silos, limit=1):
        return cls.objects.filter(silos=silos).all()[:limit]

    @classmethod
    def add_log(cls, status, description, silos):
        cls.objects.create(status=status, description=description, silos=silos)

    def __str__(self):
        return f"{self.silos.id}-{self.status}"

    class Meta:
        verbose_name_plural = "Logs"
        get_latest_by = "-time"
        ordering = ['-time']
