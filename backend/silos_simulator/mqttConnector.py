import paho.mqtt.client as paho
from paho.mqtt.client import Client
from models.silos import Silos
from os import getenv

from models.topics import Topics
from uuid import uuid4

broker = getenv("MQTT_HOST")
port = int(getenv("MQTT_PORT"))
username = getenv("MQTT_USER")
password = getenv("MQTT_PSW")


class MQTTConnector:
    def __init__(self, silos: Silos):
        self.client: Client
        self.connected = False
        self.topics = Topics()
        self.silos = silos
        self.client_id = str(uuid4())

    def on_connect(self, client, userdata, flags, rc):
        self.connected = True
        if rc == 0:
            print("Connected to MQTT Broker!")  # Not being printed in output
            if self.silos is not None:
                for topic in self.topics.subscribe:
                    self.client.subscribe(topic.substitute(silos_id=self.silos.id), qos=2)
            else:
                self.client.subscribe(self.topics.subscribe.commands.substitute(silos_id="+"), qos=2)
        else:
            print("Failed to connect, return code:", rc)

    def bootstrap_mqtt(self):
        self.client = paho.Client(client_id=self.client_id, clean_session=True)
        self.client.username_pw_set(username=username, password=password)

        self.client.on_connect = self.on_connect

        self.client.connect(host=broker, port=port, keepalive=120)

        return self
