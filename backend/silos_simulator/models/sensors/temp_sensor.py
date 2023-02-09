import datetime
import json
import random
from .sensor_interface import Sensor


class TempSensor(Sensor):
    name: str
    value: float
    min: float
    max: float
    time: float

    def __init__(self, name: str, max_val: float, min_val: float, slung: str):
        self.name = name
        self.max = max_val
        self.min = min_val
        self.slung = slung

    def get_value(self):
        self.value = random.uniform(self.min, self.max)

        return json.dumps({
            "name": self.name,
            "value": self.value,
            "time": datetime.datetime.utcnow().isoformat()
        })
