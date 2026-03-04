from vehicle import Vehicle

class Garage:
    '''
    A garage is a place that stores a collection of vehicles
    '''

    # constructor
    def __init__(self):
        '''initialize an empty list'''
    self._vehicles: list[vehicle] = []


    #g

    def add_vehicle(self, vehicle: vehicle) -> None:
        '''add a vehicle to the list'''
        self._vehicles.append(vehicle)

    def empty_garage(self):
        '''empties the garage of all the vehicles'''
        self._vehicles.clear()