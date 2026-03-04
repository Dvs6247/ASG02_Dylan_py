from vehicle import Vehicle
from manufacturer import Manufacturer
from auto_model import AutoModel

class Truck(Vehicle):
    '''
    Represents a truck type of vehicle, which may or may not be a dually.
    '''

    #
    def __init__(self,
                 manufacturer: Manufacturer,
                 model: AutoModel,
                 mpg: float
                 is_dually: bool = False,
                 ):
        super().__init__(manufacturer, model, mpg)
        self._is_dually = is_dually

        @property
        def is_dually(self) -> bool:
            return self._is_dually

        def number_of_wheels(self) -> int:
            return 6 if self._is_dually else 4

        def __str__(self) -> str:
            return (
                f"({self._manufacturer}) {self._model}, mpg: {self._mpg}
                f"is dually truck: {self._is_dually}"
                    )