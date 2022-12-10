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
             and self.cost == other.cost

    def __hash__(self):
        return hash(self.state.__str__() + str(self.directions) + str(self.cost))

    def __repr__(self):
        return self.state.__str__()