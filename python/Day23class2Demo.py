#abstraction
from abc import *
class Car(ABC):
    def __init__(self,rg):
        self.rg = rg

    def fuelTank(self):
        print('Fill the fuel into the tank')
        print('For the car with rb',str(self.rg))

    @abstractmethod
    def steering(self):
        pass

    @abstractmethod
    def company(self):
        pass