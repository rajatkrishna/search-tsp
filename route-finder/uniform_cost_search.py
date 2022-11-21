
from heapdict import heapdict   
from utils.state import State
from node import Node
from utils.stats import Stats

class Search:
    
    def findPath(self, startState : State):
        pass

class UniformCostSearch(Search):
    """
    Implementation of Uniform Cost Search using a heapdict
    as priority queue.
    """

    def __init__(self):
        self.stats = Stats()

    def findPath(self, startState : State):
        explored = []
        frontier = heapdict()
        
        if startState.isGoalState():
            self.stats.nodeCount = Node.counter
            self.stats.endTime()
            return [], self.stats
        
        node = Node(startState, [startState.currentCity], 0)
        frontier[node] = 0

        while frontier:
            currentNode = frontier.popitem()[0]
            currentState = currentNode.getCurrentState()

            if currentState not in explored:
                explored.append(currentState)

                if currentState.isGoalState():
                    self.stats.nodeCount = Node.counter
                    self.stats.endTime()
                    self.stats.totalCost = currentNode.getCost()
                    return currentNode.getDirections(), self.stats

                for (nextState, action, stepCost) in currentState.nextStates():
                    nextDirections = currentNode.getDirections() + [action]
                    # total cost upto this state
                    nextCost = currentNode.getCost() + stepCost
                    frontier[Node(nextState, nextDirections, nextCost)] = nextCost
    