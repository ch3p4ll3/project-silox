from django.apps import AppConfig
from ..utils.mqtt import client


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.api'

    def ready(self):
        client.loop_start()
