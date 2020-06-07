from abc import ABC, abstractmethod

from base.Volume import Volume


class Augmentation(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def apply(self, volume: Volume) -> Volume:
        pass

    @abstractmethod
    def randomize(self) -> None:
        pass