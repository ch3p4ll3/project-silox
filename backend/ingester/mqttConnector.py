import paho.mqtt.client as paho
from paho.mqtt.client import Client
from uuid import uuid4

broker = "localhost"
port = 1883
ca_file = "certs/file.pem"
cert_file = "certs/file.crt"
key_file = "certs/file.key"


class MQTTConnector:
    def __init__(self):
        self.client: Client
        self.connected = False
        self.client_id = str(uuid4())

    def on_connect(self, client, userdata, flags, rc):
        self.connected = True
        if rc == 0:
            print("Connected to MQTT Broker!")  # Not being printed in output
            self.client.subscribe('t/simulator/silos/+/measurements/+', qos=2)
        else:
            print("Failed to connect, return code:", rc)

    def bootstrap_mqtt(self):
        self.client = paho.Client(client_id=self.client_id, clean_session=False)

        # self.client.tls_set(
        #     ca_file,
        #     certfile=cert_file,
        #     keyfile=key_file,
        #     cert_reqs=ssl.CERT_REQUIRED,
        #     tls_version=ssl.PROTOCOL_TLSv1_2,
        #     ciphers=None
        # )

        self.client.on_connect = self.on_connect

        self.client.connect(host=broker, port=port, keepalive=120)

        return self
