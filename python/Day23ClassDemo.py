#abstraction
#class world bank sets a demand to all those classes who inherit it to have save and logo as two methods
#it has those methods too...hovever it wont show it to them
from abc import ABC, abstractmethod
class WorldBank(ABC):
    @abstractmethod
    def save(self,x):
        pass

    @abstractmethod
    def loan(self,y):
        pass

    def logo(self):
        print('Logo')

