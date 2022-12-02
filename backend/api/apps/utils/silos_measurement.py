import random
import time


class SilosMeasurement:
    temp: float
    ph: float
    int_temp: float
    ext_temp: float
    int_humidity: float
    ext_humidity: float
    int_pression: float
    co2: float
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
                    random_value = current - 0.2 + random.uniform(-0.02, 0.02)
                else:
                    random_value = current + 0.2 + random.uniform(-0.02, 0.02)

            setattr(self, var, random_value)

        self.time = time.time_ns()
