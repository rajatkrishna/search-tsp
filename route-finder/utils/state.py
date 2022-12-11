from utils.cities import Cities
from random import choice

class State:

    def isGoalState(self):
        pass

    def nextStates(self):
        pass

class SearchState(State):

    def __init__(self, visitedCities : list, pendingCities : list):
        self.visitedCities = visitedCities
        self.pendingCities = pendingCities
        self.cities = Cities()
        
        if visitedCities:  
            self.startCity = visitedCities[0]
            self.currentCity = visitedCities[-1]

    def isGoalState(self):
        """
        the goal state is reached when all cities have been visited.
        this is verified by asserting that there are no pending cities
        to visit. additionally, we should return to the starting city to 
        be successful. these two checks are performed to check for goal state.
        """
        return len(self.pendingCities) == 0\
                 and self.visitedCities\
                 and self.startCity == self.currentCity

    def nextStates(self):
        nextStates = []

        if self.isGoalState():
            return nextStates
        elif self.pendingCities:
            for city in self.pendingCities:
                visited = self.visitedCities.copy()
                pending = self.pendingCities.copy()
                visited.append(city)
                pending.remove(city)
                nextState = SearchState(visited, \
                    pending)
                stepCost = self.cities.distanceBetween(self.currentCity, city)

                nextStates.append([nextState, city, stepCost])
        else:
            visited = self.visitedCities.copy()
            visited.append(self.startCity)
            nextStates.append([SearchState(visited, []),\
                 self.startCity, self.cities.distanceBetween(self.currentCity, self.startCity)])

        return nextStates

    def findRandomChild(self):
        if self.isGoalState():
            return None
        elif self.pendingCities:
            visited = self.visitedCities.copy()
            pending = self.pendingCities.copy()
            city = choice(self.pendingCities)
            visited.append(city)
            pending.remove(city)
            stepCost = self.cities.distanceBetween(self.currentCity, city)
            return SearchState(visited, \
                    pending), stepCost
        else:
            visited = self.visitedCities.copy()
            visited.append(self.startCity)
            return SearchState(visited, []), self.cities.distanceBetween(self.currentCity, self.startCity)

    def __eq__(self, other):
        if not isinstance(other, State):
            return NotImplemented

        return self.visitedCities == other.visitedCities\
             and self.pendingCities == other.pendingCities\
             and self.currentCity == other.currentCity

    def __hash__(self):
        return hash(self.__str__())

    def __str__(self):
        return str(self.currentCity) + str(self.visitedCities) + str(self.pendingCities)