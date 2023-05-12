import datetime
import json
import random
from .sensor_interface import Sensor
from statistics import mean


# With this coefficient we can simulate a normal distribution of the values
# If Coefficient is 4, the values will be more concentrated around the mean (99.99% OK)
# If Coefficient is 3, the values will be more concentrated around the mean (99.7% OK)
# If Coefficient is 2 , the values will be more concentrated around the mean (95.4% OK)
# If Coefficient is 1, the values will be more dispersed (68.2% OK)
COEFFICIENT = 1.5


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
        """
        media = mean([self.min, self.max])
        sigma = self.max - media / COEFFICIENT
        """
        self.value = mean([self.min, self.max]) + random.gauss(mean([self.min, self.max]), 1.5)

        return json.dumps({
            "name": self.name,
            "value": self.value,
            "time": datetime.datetime.utcnow().isoformat()
        })
