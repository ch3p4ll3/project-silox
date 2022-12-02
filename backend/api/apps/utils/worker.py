from enum import Enum
from threading import Thread

import jsons
import paho.mqtt.client as mqtt
import time
from .silos_measurement import SilosMeasurement
from ..api.models.logs import Logs
from statistics import mean


class Actions(Enum):
    IDLE = 0
    FILL = 1
    EMPTY = 2


class Worker(Thread):
    def __init__(self, silos):
        self.silos = silos
        self.__silos = SilosMeasurement(silos)
        self.action = Actions.IDLE
        self.__running_worker = True
        self.__client: mqtt.Client
        self.__percentage = 100
        Thread.__init__(self)

    def __init_mqtt(self):
        self.__client = mqtt.Client()
        # client.reconnect_delay_set(min_delay=1, max_delay=120)
        self.__client.on_connect = self.__on_connect
        self.__client.on_message = self.__on_message
    
        self.__client.connect("localhost", 1883, 60)
        self.__client.loop_start()

    @staticmethod
    def __on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("info")

    @staticmethod
    def __on_message(client, userdata, msg):
        if msg.topic == 'info':
            print(msg.topic+" "+str(msg.payload))

    @property
    def __is_empty(self):
        return self.action is Actions.EMPTY and self.__silos.sensor_1 >= self.silos.height

    @property
    def __is_full(self):
        return self.action is Actions.FILL and self.__silos.sensor_1 <= 0

    @property
    def __completed(self):
        sensors = [self.__silos.sensor_1, self.__silos.sensor_2, self.__silos.sensor_3]
        sensors = [self.silos.height - i for i in sensors]
        cur_percentage = (mean(sensors) / self.silos.height) * 100
        return self.action is not Actions.IDLE and int(cur_percentage) - 5 <= self.__percentage <= int(cur_percentage) + 5

    def set_idle_level(self):
        sensors = [self.__silos.sensor_1, self.__silos.sensor_2, self.__silos.sensor_3]

        if self.action is Actions.FILL:
            if self.__is_full:
                self.__silos.sensor_1 = self.__silos.sensor_2 = self.__silos.sensor_3 = 0
                return
        else:
            if self.__is_empty:
                self.__silos.sensor_1 = self.__silos.sensor_2 = self.__silos.sensor_3 = self.silos.height
                return

        self.__silos.sensor_1 = self.__silos.sensor_2 = self.__silos.sensor_3 = mean(sensors)

    def run(self) -> None:
        self.__init_mqtt()
        while self.__running_worker:
            if self.__is_empty or self.__is_full or self.__completed:  # se è pieno o vuoto oppure completato andare in idle
                Logs(status='Stopped', description='emptying/filling stopped: Level reached', silos=self.silos).save()
                self.set_idle_level()
                self.action = Actions.IDLE

            if self.action is Actions.IDLE:
                self.__silos.idle()
            
            elif self.action is Actions.EMPTY:
                self.__silos.empty()
            
            elif self.action is Actions.FILL:
                self.__silos.fill()

            data = jsons.dumps(self.__silos)
            self.__client.publish('t/measurement', data)

            time.sleep(1)
    
    def stop(self):
        self.action = Actions.IDLE
        Logs(status='IDLE', description='Worker is in IDLE', silos=self.silos).save()
    
    def fill(self, percentage: int = 100):
        self.action = Actions.FILL
        self.__percentage = percentage
        Logs(status='FILL', description=f'Starting filling until {percentage}% is reached', silos=self.silos).save()

    def empty(self, percentage: int = 0):
        self.action = Actions.EMPTY
        self.__percentage = percentage
        Logs(status='EMPTY', description=f'Starting emptying until {percentage}% is reached', silos=self.silos).save()
    
    def stop_worker(self):
        self.__running_worker = False
        self.__client.disconnect()
        self.__client.loop_stop()
        Logs(status='Stopped', description='Worker Stopped', silos=self.silos).save()

    def __eq__(self, other):
        return self.silos.id == other.silos.id

    def __hash__(self):
        return hash(self.__silos)
