from importlib.resources import files
import math

class Cities:

    def __init__(self):
        """
        loads the list of cities and tokenizes them. 
        -------------
        returns a list of triplets where each element
        represents a city index to identify the city,
        and the x,y coordinates of that city.
        """
        
        citiesListStr = files('resources').joinpath('cities.txt').read_text()
        entries = citiesListStr.split('\n')
        self.cities = {int(city.split(' ')[0]): (int(city.split(' ')[1]), int(city.split(' ')[2])) for city in entries}

    def getCities(self) -> list:
        return self.cities
    
    def distanceBetween(self, source, dest):
        """
        accepts two city indices that represent two cities
        --------------
        returns the euclidean distance between 
        the sources and destinations.
        --------------
        """

        sourceX, sourceY = self.cities[source]
        destX, destY = self.cities[dest]

        return math.sqrt((sourceX - destX)**2 + (sourceY - destY)**2)

        