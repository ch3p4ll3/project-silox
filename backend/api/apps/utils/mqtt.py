import paho.mqtt.client as mqtt
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


def on_connect(mqtt_client, user_data, flags, rc):
    if rc == 0:
        logger.info('Connected to MQTT broker')


client = mqtt.Client(clean_session=True)
client.on_connect = on_connect
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PSW)
client.connect(
    host=settings.MQTT_HOST,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEP_ALIVE
)
