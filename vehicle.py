from abc import ABC, abstractmethod
from functools import total_ordering 

from manufacturer import Manufacturer
#from

class Vehicle(ABC):
    '''
    Abstract base class (ABC) for all vehicles
    '''

    # manufacturer
    def __init__(self,
                 manufacturer: Manufacturer,
                 model: AutoModel,
                 mpg: float):
        self.manufacturer = manufacturer
        self.model = model
        self.mpg = mpg

    @property
    def manufacturer(self) -> Manufacturer:
        return self._manufacturer
    
    @property
    def model(self) -> AutoModel:
        return self._model
    
    @property
    def mpg(self) -> float:
        return self.mpg
    
    @property
    def release_year(self) -> int:

    #---------concrete method--------------
class Vehicle(ABC):
    def how_far_with(self,
                     num_of_gallons: int) -> float
        return self.mpg
    
    #----------abstract method------------
    def number_of_wheels(self): -> int:
        

# ---- comparison crtieria ------
def __eq__(self, other) -> bool:
    return self.release_year == other.release_year

def __it__(self, other) -> bool:
    pass

def __hash__(self) -> int:
    pass