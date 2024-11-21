from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
