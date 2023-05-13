import paho.mqtt.client as paho
from paho.mqtt.client import Client
from uuid import uuid4
from os import getenv

broker = getenv("MQTT_HOST")
port = int(getenv("MQTT_PORT"))
username = getenv("MQTT_USER")
password = getenv("MQTT_PSW")


class MQTTConnector:
    def __init__(self):
        self.client: Client
        self.connected = False
        self.client_id = str(uuid4())

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:  # Connection successful
            self.connected = True
            print("Connected to MQTT Broker!")
            self.client.subscribe('t/simulator/silos/+/measurements/+', qos=2)  # Subscribe to all measurements
        else:
            print("Failed to connect, return code:", rc)

    def bootstrap_mqtt(self):
        """Connects to the MQTT broker and subscribes to the topics"""
        self.client = paho.Client(client_id=self.client_id, clean_session=False)
        self.client.username_pw_set(username=username, password=password)

        self.client.on_connect = self.on_connect

        self.client.connect(host=broker, port=port, keepalive=120)

        return self
