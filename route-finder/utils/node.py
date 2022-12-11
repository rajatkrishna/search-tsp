class Node:

    counter = 0

    def __init__(self, state, directions, cost):
        self.state = state
        self.directions = directions
        self.cost = cost
        Node.counter += 1

    def getCurrentState(self):
        return self.state

    def getDirections(self):
        return self.directions
    
    def getCost(self):
        return self.cost

    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented

        return self.state == other.state\
             and self.directions == other.directions\
             and round(self.cost, 5) == round(other.cost, 5)

    def __hash__(self):
        return hash(self.__str__())

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.state.__str__() + str(self.directions) + str(round(self.cost, 5))