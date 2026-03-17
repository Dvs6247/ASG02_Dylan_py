from abc import ABC, abstractmethod
from functools import total_ordering 
from manufacturer import Manufacturer
from auto_model import AutoModel

@total_ordering
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
        """Return the first production year from the model."""
        return self._model.first_year

    #---------concrete method--------------
    def how_far_with(self,num_of_gallons: int) -> float:
        '''Return the number of miles this vehicle can travel.'''
        return self.mpg * num_of_gallons
    
    #----------abstract method------------
    def number_of_wheels(self) -> int:
        '''Return the nmber of wheels for this vehicle.'''

# ---- comparison crtieria ------
def __eq__(self, other) -> bool:
    if not isinstance(other, Vehicle):
        return NotImplemented
    return self.release_year == other.release_year

def __it__(self, other) -> bool:
    pass 
    if not isinstance(other, Vehicle):
        return NotImplemented
    return self.release_year < other.release_year

def __hash__(self) -> int:
    return hash(self.release_year)
