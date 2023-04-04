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
    slug: str

    def __init__(self, name: str, max_val: float, min_val: float, slug: str):
        self.name = name
        self.max = max_val
        self.min = min_val
        self.slug = slug

    def get_value(self):
        self.value = random.uniform(self.min, self.max)

        return json.dumps({
            "name": self.name,
            "value": self.value,
            "time": datetime.datetime.utcnow().isoformat()
        })
