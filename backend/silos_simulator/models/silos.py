import math
from dataclasses import dataclass


@dataclass
class Size:
    height: float
    diameter: float


@dataclass
class Silos:
    id: str
    size: Size

    @property
    def volume(self):
        return self.size.height * self.size.diameter ** 2 * math.pi / 4
