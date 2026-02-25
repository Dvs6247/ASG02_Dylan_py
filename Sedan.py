from vehicle import Vehicle
from manufacturer import Manufacturer
from auto_model import AutoModel

class Sedan(Vehicle):
    '''
    Represents a sedan type of vehicle
    '''

    #
    def __init__(self,
                 manufacturer: Manufacturer,
                 model: AutoModel,
                 )