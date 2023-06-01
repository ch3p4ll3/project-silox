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
    """Enum for the possible actions that the simulator can do"""
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
        """Callback for when a message is received from the broker"""
        payload: dict = Utils.decode_payload(message.payload.decode())  # Decode the payload

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
        
        elif message.topic == Utils.get_subscribe_topic(self.silos, Topics.subscribe.stop_simulation):
            self.stop_simulation()

    def __is_not_full(self, level_sensor):
        """Returns true if the silos is not full, false otherwise"""
        return self.level > (1 - level_sensor.value / self.silos.size.height) * 100

    def __is_not_empty(self, level_sensor):
        """Returns true if the silos is not empty, false otherwise"""
        return self.level < (1 - (level_sensor.value / self.silos.size.height)) * 100

    def run(self):
        """Starts the simulator thread"""
        self.__init_mqtt()
        while not self.to_kill:
            while self.is_running:
                for sensor in self.silos.sensors:  # For each sensor, publish its value
                    topic = Utils.get_publish_topic(self.silos, sensor, Topics.publish.topic)
                    self.protocol.client.publish(topic, sensor.get_value(), 2)

                for level_sensor in self.silos.level_sensor:  # For each level sensor, publish its value
                    topic = Utils.get_publish_topic(self.silos, level_sensor, Topics.publish.topic)

                    if self.actions is Actions.FILL:  # If the silos is filling, increase the level
                        if self.__is_not_full(level_sensor):
                            level_sensor.value -= random.uniform(0.05, 0.1)  # Randomly decrease the level of the silos
                        else:
                            self.actions = Actions.IDLE  # If the silos is full, stop filling

                    elif self.actions is Actions.EMPTY:  # If the silos is emptying, decrease the level
                        if self.__is_not_empty(level_sensor):
                            level_sensor.value += random.uniform(0.05, 0.1)  # Randomly increase the level of the silos
                        else:
                            self.actions = Actions.IDLE  # If the silos is empty, stop emptying

                    self.protocol.client.publish(topic, level_sensor.get_value(), qos=2)  # Publish the value

                time.sleep(1)

    def __init_mqtt(self):
        self.protocol.client.on_message = self.on_message
        self.protocol.client.loop_start()

    def fill(self, payload: dict):
        """Fills the silos with the given percentage of the silos"""
        self.level = payload.get('percentage', 100)
        self.actions = Actions.FILL

    def empty(self, payload: dict):
        """Empties the silos with the given percentage of the silos"""
        self.level = payload.get('percentage', 0)
        self.actions = Actions.EMPTY

    def idle(self):
        self.actions = Actions.IDLE

    def kill(self, payload: dict):
        """Kills the simulator"""
        if payload.get('kill'):  # If the payload contains the kill key, kill the simulator and disconnect from the broker
            self.is_running = False
            self.to_kill = True
            self.protocol.client.loop_stop()
            self.protocol.client.disconnect()

    def start_simulation(self):
        self.is_running = True

    def stop_simulation(self):
        self.is_running = False
