from paho.mqtt.client import MQTTMessage
from influx_management import InfluxDb
from mqttConnector import MQTTConnector
from utils import Utils


class Ingester:
    def __init__(self):
        self.mqtt_connector = MQTTConnector().bootstrap_mqtt()
        self.mqtt_connector.client.on_message = self.on_message
        self.mqtt_connector.client.loop_forever()

    def on_message(self, client, boh, message: MQTTMessage):
        silos_id = message.topic.split('/')[3]
        slung = message.topic.split('/')[-1]

        with InfluxDb() as influx:
            influx.write(
                silos_id,
                slung,
                Utils.decode_payload(message.payload.decode())
            )
