class AutoModel:
    """
    Represents an automobile model with production-year information
    """
    def __init__(self, name: str, in_production: bool, years):
        if not years:
            raise ValueError("The years list must be non-empty")
        self._name = name
        self._in_production = in_production
        self._years = list(years) #defensive copy
        
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def in_production(self) -> bool:
        return self._in_production
    
    @property 
    def years(self) -> list[int]:
        return list(self._years) #return a copy
    
    @property
    def first_year(self) -> int:
        '''Return the first (earliest) production year.'''
        return self._years[0]
    
    def __str__(self) -> str:
        return (
            f"{self._name} in production = {self._in__production}"
            f" release year: {self._years[0]}"
        )