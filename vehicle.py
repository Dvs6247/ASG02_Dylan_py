from abc import ABC, abstractmethod
# from

from manufacturer import Manufacturer

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
    def mpg(self) = float:
        return self.mpg
    
    #---------concrete method--------------
    def how_far_with(self,
                     num_of_gallons: int) -> float
    
    def number_of_wheels: