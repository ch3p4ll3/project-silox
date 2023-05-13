import json

from models.sensors.sensor_interface import Sensor
from models.silos import Silos

from string import Template


class Utils:
    @staticmethod
    def get_publish_topic(silos: Silos, sensor: Sensor, template: Template):
        """Returns the topic to publish to, given a silos and a sensor"""
        return template.substitute(
            silos_id=silos.id,
            slug=sensor.slug
        )

    @staticmethod
    def get_subscribe_topic(silos: Silos, template: Template):
        """Returns the topic to subscribe to, given a silos"""
        return template.substitute(
            silos_id=silos.id
        )

    @staticmethod
    def decode_payload(payload: str):
        """Decodes the payload from a string to a dictionary"""
        try:
            return json.loads(payload)
        except json.JSONDecodeError:
            return {}
