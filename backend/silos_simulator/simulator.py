import random
import time
from threading import Thread

from enum import Enum
from mqttConnector import MQTTConnector
from models.silos import Silos
from paho.mqtt.client import MQTTMessage
from models.topics import Topics

from utils import Utils


class Actions(Enum):
    IDLE = 0
    FILL = 1
    EMPTY = 2


class Simulator(Thread):
    def __init__(self, silos: Silos):
        self.silos = silos
        self.is_running = True
        self.to_kill = False
        self.actions: Actions = Actions.IDLE
        self.protocol = MQTTConnector(self.silos).bootstrap_mqtt()
        self.level: float = 0
        Thread.__init__(self)

    def on_message(self, client, boh, message: MQTTMessage):
        payload: dict = Utils.decode_payload(message.payload.decode())

        if message.topic == Utils.get_subscribe_topic(self.silos, Topics.subscribe.kill):
            self.kill(payload)

        elif message.topic == Utils.get_subscribe_topic(self.silos, Topics.subscribe.fill):
            self.fill(payload)

        elif message.topic == Utils.get_subscribe_topic(self.silos, Topics.subscribe.empty):
            self.empty(payload)

        elif message.topic == Utils.get_subscribe_topic(self.silos, Topics.subscribe.idle):
            self.idle()

        elif message.topic == Utils.get_subscribe_topic(self.silos, Topics.subscribe.start_simulation):
            self.start_simulation()
        
        elif message.topic == Utils.get_subscribe_topic(self.silos, Topics.subscribe.kill):
            self.stop_simulation()

    def __is_not_full(self, level_sensor):
        return self.level > (1 - level_sensor.value / self.silos.size.height) / 100

    def __is_not_empty(self, level_sensor):
        return self.level < (1 - level_sensor.value / self.silos.size.height) * 100

    def run(self):
        self.__init_mqtt()
        while not self.to_kill:
            while self.is_running:
                for sensor in self.silos.sensors:
                    topic = Utils.get_publish_topic(self.silos, sensor, Topics.publish.topic)
                    self.protocol.client.publish(topic, sensor.get_value(), 2)

                for level_sensor in self.silos.level_sensor:
                    topic = Utils.get_publish_topic(self.silos, level_sensor, Topics.publish.topic)

                    if self.actions is Actions.FILL:
                        if self.__is_not_full(level_sensor):
                            level_sensor.value -= random.uniform(0.05, 0.1)
                        else:
                            self.actions = Actions.IDLE

                    elif self.actions is Actions.EMPTY:
                        if self.__is_not_empty(level_sensor):
                            level_sensor.value += random.uniform(0.05, 0.1)
                        else:
                            self.actions = Actions.IDLE

                    self.protocol.client.publish(topic, level_sensor.get_value(), qos=2)

                time.sleep(1)

    def __init_mqtt(self):
        self.protocol.client.on_message = self.on_message
        self.protocol.client.loop_start()

    def fill(self, payload: dict):
        self.level = payload.get('percentage', 100)
        self.actions = Actions.FILL

    def empty(self, payload: dict):
        self.level = payload.get('percentage', 0)
        self.actions = Actions.EMPTY

    def idle(self):
        self.actions = Actions.IDLE

    def kill(self, payload: dict):
        if payload.get('kill'):
            self.is_running = False
            self.to_kill = True
            self.protocol.client.loop_stop()
            self.protocol.client.disconnect()

    def start_simulation(self):
        self.is_running = True

    def stop_simulation(self):
        self.is_running = False
