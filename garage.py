from vehicle import Vehicle

class Garage:
    '''
    A garage is a place that stores a collection of vehicles
    '''

    # constructor
    def __init__(self):
        '''initialize an empty list'''
        self._vehicles: list[Vehicle] = []
#Added a list for the vehicles along with an add, remove, and sort function to the garage.
    @property
    def vehicles(self) -> list[Vehicle]:
        '''Return a copy of the internal vehicles list.'''
        return list(self._vehicles)

    def add_vehicle(self, vehicle: Vehicle) -> None:
        '''add a vehicle to the list'''
        self._vehicles.append(vehicle)

    def empty_garage(self):
        '''empties the garage of all the vehicles'''
        self._vehicles.clear()

    def sort_by_released_year(self) -> None:
        '''Sort vehicles in place by release year.'''
        self._vehicles.sort()

    def __str__(self) -> str:
        return '\n'.join(str(v) for v in self._vehicles)
    