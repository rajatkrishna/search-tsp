from utils.cities import Cities

class State:

    def isGoalState(self):
        pass

    def nextStates(self):
        pass

class UcsState(State):

    def __init__(self, visitedCities : list, pendingCities : list):
        self.visitedCities = visitedCities
        self.pendingCities = pendingCities
        self.cities = Cities()
        
        if visitedCities:  
            self.startCity = visitedCities[0]
            self.currentCity = visitedCities[len(visitedCities) - 1]

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
                nextState = UcsState(visited, \
                    pending)
                stepCost = self.cities.distanceBetween(self.currentCity, city)

                nextStates.append([nextState, city, stepCost])
        else:
            self.visitedCities.append(self.startCity)
            nextStates.append([UcsState(self.visitedCities, []),\
                 self.startCity, self.cities.distanceBetween(self.currentCity, self.startCity)])

        return nextStates

    def __str__(self):
        return "Current city: " + str(self.currentCity) + "\nVisited cities: "\
             + str(self.visitedCities) + "\nPending cities: " + str(self.pendingCities)