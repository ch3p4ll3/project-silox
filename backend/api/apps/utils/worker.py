import time
import random

import jsons
import paho.mqtt.client as mqtt
from threading import Thread


class SilosMeasurement:
    temp: float
    ph: float
    int_temp: float
    ext_temp: float
    int_humidity: float
    ext_humidity: float
    int_pression: float
    id: int
    sensor_1: float
    sensor_2: float
    sensor_3: float
    time: int

    def __init__(self, silos):
        self.id = silos.id
        self.sensor_1: float = silos.height  # stato iniziale sensori. Se = altezza silos, allora il silos è vuoto
        self.sensor_2: float = silos.height
        self.sensor_3: float = silos.height

    def fill(self):
        self.__generate(idle=False, fill=True)

    def empty(self):
        self.__generate(idle=False, fill=False)

    def idle(self):
        self.__generate(idle=True)

    def __generate(self, idle: bool = False, fill: bool = True):
        for var, var_type in self.__annotations__.items():
            random_value = None

            if var == 'id' or (idle and var.startswith("sensor_")):
                continue

            if var_type is int:
                random_value = random.randint(1, 10)

            elif var_type is float:
                random_value = random.uniform(1.0, 25.0)

            if var.startswith("sensor_"):  # modifica valori sensori solo se ci sono cambi di stato(fill/empty)
                current = getattr(self, var)
                if fill:
                    random_value = current - 1.2 + random.uniform(-0.2, 0.2)
                else:
                    random_value = current + 1.2 + random.uniform(-0.2, 0.2)

            setattr(self, var, random_value)

        self.time = time.time_ns()


class Worker:
    '''
    Worker di un silos, metodi per riempire, svuotare o stoppare qualsiasi evento

    riempimento e svuotimento fanno partire dei thread per l'azionamento
    '''
    def __init__(self, silos):
        self.silos_obj = silos
        self.silos = SilosMeasurement(silos)
        self.running = False
        self.thread = None

        self.__init_mqtt()
        Thread(target=self.__idle).start()

    def __init_mqtt(self):
        self.client = mqtt.Client()
        self.client.reconnect_delay_set(min_delay=1, max_delay=120)
        self.client.on_connect = self.__on_connect
        self.client.on_message = self.__on_message

        self.client.connect("localhost", 1883, 60)
        self.client.loop_start()

    def __idle(self):
        while True:
            if not self.running:  # Manda dati solo se nessun altro thread è attivo
                self.silos.idle()
                data = jsons.dumps(self.silos)
                self.client.publish('t/measurement', data)

            time.sleep(.5)

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

    def fill(self):
        if self.thread is not None:  # se è in corso un'altra operazione bloccala
            self.stop()

        self.running = True
        self.thread = Thread(target=self.__fill)
        self.thread.start()

    def __fill(self):
        while self.running:
            self.silos.fill()
            data = jsons.dumps(self.silos)
            self.client.publish('t/measurement', data)

            time.sleep(1)

    def empty(self):
        if self.thread is not None:
            self.stop()
        self.running = True
        self.thread = Thread(target=self.__empty)
        self.thread.start()

    def __empty(self):
        while self.running:
            self.silos.empty()
            data = jsons.dumps(self.silos)
            self.client.publish('t/measurement', data)

            time.sleep(1)

    def stop(self):
        if self.thread:
            while self.thread.is_alive():
                self.running = False

        self.running = False
        print("stopped")


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
