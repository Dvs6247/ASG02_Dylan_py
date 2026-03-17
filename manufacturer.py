class Manufacturer:
    '''
    Represents a vehicle manufacturer.
    '''

    #constructor
    def __init__(self, name: str, country: str):
        self._name = name
        self._country = country
    
    #properties
    @property
    def get_name(self) -> str:
        return self._name 
    
    @property
    def get_country(self) -> str:
        return self._country
    
    def __str__(self) -> str:
        return f"{self._name}, {self._country}"
    