from mqttConnector import MQTTConnector
from paho.mqtt.client import MQTTMessage
from typing import List

from simulator import Simulator
from models.silos import Silos, Size
from models.sensors import TempSensor, LevelSensor

from utils import Utils


class MqttListener:
    def __init__(self):
        self.simulators: List[Simulator] = []
        self.protocol = MQTTConnector(None).bootstrap_mqtt()

    def __init_mqtt(self):
        self.protocol.client.on_message = self.on_message
        self.protocol.client.loop_forever()

    def __get_silos(self, payload: dict):
        sensors = [sensor for sensor in payload['sensors'] if sensor['sensor']['sensor_type'] != 'level']
        sensors = [
            TempSensor(
                sensor['sensor']['sensor_name'],
                sensor['sensor']['max_value'],
                sensor['sensor']['min_value'],
                sensor['sensor']['sensor_slug']
            ) for sensor in sensors
        ]

        level_sensors = [sensor for sensor in payload['sensors'] if sensor['sensor']['sensor_type'] == 'level']

        level_sensors = [
            LevelSensor(
                sensor['sensor']['sensor_name'],
                sensor['sensor']['max_value'],
                sensor['sensor']['min_value'],
                sensor['sensor']['sensor_slug']
            ) for sensor in level_sensors
        ]

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
        return any([simulator.silos.id == silos_id for simulator in self.simulators])

    def on_message(self, client, boh, message: MQTTMessage):
        payload: dict = Utils.decode_payload(message.payload.decode())

        if message.topic.endswith("start"):
            silos = self.__get_silos(payload)

            if not self.__silos_already_running(silos.id):
                simulator = Simulator(silos)
                simulator.start()
                self.simulators.append(simulator)

        elif message.topic.endswith("kill"):
            silos = next((simulator for simulator in self.simulators if simulator.silos.id == payload['id']), None)

            if silos:
                self.simulators.remove(silos)

    def run(self):
        self.__init_mqtt()
