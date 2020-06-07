import numpy as np

from base.Augmentation import Augmentation
from base.Volume import Volume


class AddUniformNoise(Augmentation):
    def __init__(self, low: float, high: float, size: tuple):
        super().__init__()
        self.low = low
        self.high = high
        self.size = size
        self.noise = None
        self.randomize()

    def randomize(self) -> None:
        self.noise = np.random.uniform(self.low, self.high, self.size)

    def apply(self, volume: Volume) -> Volume:
        return volume + self.noise
