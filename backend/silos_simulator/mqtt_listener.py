from mqttConnector import MQTTConnector
from paho.mqtt.client import MQTTMessage
from typing import List

from simulator import Simulator
from models.silos import Silos, Size
from models.sensors import TempSensor, LevelSensor

from utils import Utils


class MqttListener:
    def __init__(self):
        self.simulators: List[Simulator] = []  # List of running simulators
        self.protocol = MQTTConnector(None).bootstrap_mqtt()

    def __init_mqtt(self):
        """Initialize MQTT connection"""
        self.protocol.client.on_message = self.on_message
        self.protocol.client.loop_forever()

    def __get_silos(self, payload: dict):
        """Get Silos object from payload"""

        sensors = [sensor for sensor in payload['sensors'] if sensor['sensor_type'] != 2]

        # Create list of TempSensor objects from payload
        sensors = [
            TempSensor(
                sensor['sensor_name'],
                sensor['max_value'],
                sensor['min_value'],
                sensor['sensor_slug']
            ) for sensor in sensors
        ]

        level_sensors = [sensor for sensor in payload['sensors'] if sensor['sensor_type'] == 2]

        # Create list of LevelSensor objects from payload
        level_sensors = [
            LevelSensor(
                sensor['sensor_name'],
                sensor['max_value'],
                sensor['min_value'],
                payload['size']['height'],
                sensor['sensor_slug']
            ) for sensor in level_sensors
        ]

        # Create Silos object from payload and return it
        return Silos(
            payload.pop("id"),
            Size(
                payload['size'].pop("height"),
                payload['size'].pop("diameter")
            ),
            sensors,
            level_sensors
        )

    def __silos_already_running(self, silos_id) -> bool:
        """Check if silos is already running"""
        return any([simulator.silos.id == silos_id for simulator in self.simulators])

    def on_message(self, client, boh, message: MQTTMessage):
        """Callback for MQTT for handling messages"""
        payload: dict = Utils.decode_payload(message.payload.decode())

        if message.topic.endswith("start"):  # Check if topic ends with "start"
            silos = self.__get_silos(payload)

            if silos.id == -1:  # if id is -1 do nothing(esp 32 silos id)
                return

            if not self.__silos_already_running(silos.id):  # Check if silos is already running
                simulator = Simulator(silos)  # Create simulator and start it in a new thread
                simulator.start()
                self.simulators.append(simulator)  # Add simulator to list of running simulators

        elif message.topic.endswith("kill"):  # Check if topic ends with "kill"
            # Get simulator from list of running simulators
            silos = next((simulator for simulator in self.simulators if simulator.silos.id == payload['id']), None)

            if silos:  # If simulator exists, stop it and remove it from list of running simulators
                self.simulators.remove(silos)

    def run(self):
        self.__init_mqtt()
