from abc import ABC, abstractmethod
from .DataSaver import DataSaver

class Saveable(ABC):
    @abstractmethod
    def load(self, data_saver: DataSaver):
        pass

    def save(self, data_saver: DataSaver):
        pass