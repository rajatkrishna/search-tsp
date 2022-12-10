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
