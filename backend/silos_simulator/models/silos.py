import math
from typing import List
from dataclasses import dataclass

from .sensors.sensor_interface import Sensor


@dataclass
class Size:
    height: float
    diameter: float


@dataclass
class Silos:
    id: str
    size: Size
    sensors: List[Sensor]
    level_sensor: List[Sensor]

    @property
    def volume(self):
        return self.size.height * self.size.diameter ** 2 * math.pi / 4
