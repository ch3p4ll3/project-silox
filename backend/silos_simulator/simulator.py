import random
import time
import json
from threading import Thread

from enum import Enum
from models.sensors import TempSensor, LevelSensor
from mqttConnector import MQTTConnector
from models.silos import Silos
from paho.mqtt.client import MQTTMessage
from topics import Topics


class Actions(Enum):
    IDLE = 0
    FILL = 1
    EMPTY = 2


class Simulator(Thread):
    def __init__(self, silos: Silos):
        self.silos = silos
        self.is_running = True
        self.actions: Actions = Actions.IDLE
        self.protocol = MQTTConnector(self.silos).bootstrap_mqtt()
        self.sensors = [
            TempSensor('Internal Temperature', 30, 20, "int_temp"),
            TempSensor('External Temperature', 30, 20, "ext_temp"),
        ]
        self.level_sensors = [
            LevelSensor('Level Sensor 1', self.silos.size.height, 0, 'level_1'),
            LevelSensor('Level Sensor 2', self.silos.size.height, 0, 'level_2')
        ]
        self.level: float = 0
        Thread.__init__(self)

    def on_message(self, client, boh, message: MQTTMessage):
        payload: dict = json.loads(message.payload.decode())

        if message.topic == self.protocol.topics.subscribe.kill:
            self.kill(payload)

        elif message.topic == self.protocol.topics.subscribe.fill:
            self.fill(payload)

        elif message.topic == self.protocol.topics.subscribe.empty:
            self.empty(payload)

        elif message.topic == self.protocol.topics.subscribe.idle:
            self.idle(payload)

    def run(self):
        self.__init_mqtt()
        while self.is_running:
            for sensor in self.sensors:
                topic = Topics(self.silos.id, sensor.slung).publish.topic
                self.protocol.client.publish(topic, sensor.get_value(), 2)

            for level_sensor in self.level_sensors:
                topic = Topics(self.silos.id, level_sensor.slung).publish.topic
                if self.actions is Actions.FILL:
                    if self.level > (1 - level_sensor.value / self.silos.size.height) / 100:
                        level_sensor.value -= random.uniform(0.05, 0.1)
                    else:
                        self.actions = Actions.IDLE

                elif self.actions is Actions.EMPTY:
                    if self.level < (1 - level_sensor.value / self.silos.size.height) * 100:
                        level_sensor.value += random.uniform(0.05, 0.1)
                    else:
                        self.actions = Actions.IDLE

                self.protocol.client.publish(topic, level_sensor.get_value(), 2)

            time.sleep(1)

    def __init_mqtt(self):
        self.protocol.client.on_message = self.on_message
        self.protocol.client.loop_start()

    def fill(self, payload: dict):
        self.level = payload.get('percentage') or 100
        self.actions = Actions.FILL

    def empty(self, payload: dict):
        self.level = payload.get('percentage') or 0
        self.actions = Actions.EMPTY

    def idle(self, payload: dict):
        self.actions = Actions.IDLE

    def kill(self, payload: dict):
        if payload.get('kill'):
            self.is_running = False
            self.protocol.client.loop_stop()
            self.protocol.client.disconnect()
