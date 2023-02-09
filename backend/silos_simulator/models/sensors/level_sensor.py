import datetime
import json
import random
from .sensor_interface import Sensor


class LevelSensor(Sensor):
    name: str
    value: float
    min: float
    max: float
    time: float

    def __init__(self, name: str, max_val: float, min_val: float, slung: str):
        self.name = name
        self.value = max_val
        self.max = max_val
        self.min = min_val
        self.slung = slung

    def get_value(self):
        return json.dumps({
            "name": self.name,
            "value": self.value,
            "time": datetime.datetime.utcnow().isoformat()
        })
