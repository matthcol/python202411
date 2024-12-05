from dataclasses import dataclass

@dataclass
class City:
    name: str
    zipcode: str
    population: int|None = None

    def department(self) -> str:
        """extract department number from zipcode
        
        NB: 
        - if zipcode starts with 97|98, department has 3 digits
        - if zipcode has 5 digits, department has 2 digits|characters
        - Corse departments are 2A and 2B
        """
        dept = self.zipcode[:2]
        # TODO improve code
        return dept
    
    def incr_population(self, delta: int):
        if self.population is not None:
            self.population += delta

    @staticmethod # or @classmethod
    def parse(city_str: str) -> 'City':
        """convert a text representing a city to a new instance City
        
        Text format: name,zipcode,population

        Example: Toulouse,31000,77000
        """
        name, zipcode, population_str = city_str.split(',')
        population_int_or_none = int(population_str)
        return City(name=name,zipcode=zipcode, population=population_int_or_none)
