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
        """The callback for when a PUBLISH message is received from the server."""
        silos_id = message.topic.split('/')[3]  # get the silos id from the topic
        slug = message.topic.split('/')[-1]  # get the sensor slug from the topic

        with InfluxDb() as influx:  # write the payload to the database
            influx.write(
                silos_id,
                slug,
                Utils.decode_payload(message.payload.decode())
            )
