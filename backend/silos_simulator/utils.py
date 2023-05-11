import json

from models.sensors.sensor_interface import Sensor
from models.silos import Silos

from string import Template


class Utils:
    @staticmethod
    def get_publish_topic(silos: Silos, sensor: Sensor, template: Template):
        return template.substitute(
            silos_id=silos.id,
            slug=sensor.slug
        )

    @staticmethod
    def get_subscribe_topic(silos: Silos, template: Template):
        return template.substitute(
            silos_id=silos.id
        )

    @staticmethod
    def decode_payload(payload: str):
        try:
            return json.loads(payload)
        except json.JSONDecodeError:
            return {}
