# import time
# import random
# import jsons
# 
# import paho.mqtt.client as mqtt
# 
# 
# class Silos:
#     id: int
#     temp: float
#     ph: float
#     int_temp: float
#     ext_temp: float
#     int_humidity: float
#     ext_humidity: float
#     int_pression: float
#     sensor_1: float = 25  # stato iniziale sensori. Se = altezza silos, allora il silos è vuoto
#     sensor_2: float = 25
#     sensor_3: float = 25
#     time = None
# 
#     def riempi(self):
#         for var, var_type in self.__annotations__.items():
#             random_value = None
# 
#             if var_type is int:
#                 random_value = random.randint(1, 10)
# 
#             elif var_type is float:
#                 random_value = random.uniform(1.0, 25.0)
# 
#             if var.startswith("sensor_"):
#                 current = getattr(self, var)
#                 random_value = current - 1.2 + random.uniform(-0.2, 0.2)
# 
#             setattr(self, var, random_value)
# 
#         self.time = time.time_ns()
#         self.id = 1
# 
# 
# # The callback for when the client receives a CONNACK response from the server.
# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code "+str(rc))
# 
#     # Subscribing in on_connect() means that if we lose the connection and
#     # reconnect then subscriptions will be renewed.
#     client.subscribe("info")
# 
# # The callback for when a PUBLISH message is received from the server.
# 
# 
# def on_message(client, userdata, msg):
#     if msg.topic == 'info':
#         print(msg.topic+" "+str(msg.payload))
# 
# 
# client = mqtt.Client()
# client.reconnect_delay_set(min_delay=1, max_delay=120)
# client.on_connect = on_connect
# client.on_message = on_message
# 
# client.connect("localhost", 1883, 60)
# 
# 
# client.loop_start()
# 
# a = Silos()
# 
# try:
#     while True:
#         a.riempi()
#         data = jsons.dumps(a)
# 
#         client.publish('t/measurement', data)
#         time.sleep(.5)
# 
# except KeyboardInterrupt:
#     client.disconnect()
#     client.loop_stop()
from enum import Enum
from threading import Thread

import jsons
import paho.mqtt.client as mqtt
import time
from .silos_measurement import SilosMeasurement


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

    def run(self) -> None:
        self.__init_mqtt()
        while self.__running_worker:
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
    
    def fill(self):
        self.action = Actions.FILL
    
    def empty(self):
        self.action = Actions.EMPTY
    
    def stop_worker(self):
        self.__running_worker = False
        self.__client.disconnect()
        self.__client.loop_stop()

    def __eq__(self, other):
        return self.silos.id == other.silos.id

    def __hash__(self):
        return hash(self.__silos)
