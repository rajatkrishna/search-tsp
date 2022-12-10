
from heapdict import heapdict   
from utils.state import State
from utils.node import Node
from utils.stats import Stats
from collections import defaultdict
from math import log, sqrt
from utils.logger import Logger

class Search:
    
    def findPath(self, startState : State):
        pass

class UniformCostSearch(Search):
    """
    Implementation of Uniform Cost Search using a heapdict
    as priority queue.
    """

    def __init__(self, logEnable):
        self.stats = Stats()
        self.logger = Logger(logEnable)

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
    
class MCTS(Search):
    """
    Implementation of Monte-Carlo Tree Search algorithm.
    """

    def __init__(self, logEnable = False, expWeight = 1):
        self.rewards = defaultdict(int)
        self.counts = defaultdict(int)
        self.children = dict()
        self.expWeight = expWeight
        self.logger = Logger(logEnable)
        self.stats = Stats()
        
    def findPath(self, startState: State):
        node = Node(startState, [startState.currentCity], 0)

        self.logger.log("Starting at city: ", startState.currentCity)

        while True:
            for _ in range(50):
                self.doRollout(node)

            node = self.choose(node)

            if node.state.isGoalState():
                self.stats.nodeCount = Node.counter
                self.stats.endTime()
                self.stats.totalCost = node.getCost()
                return node.state.visitedCities, self.stats

    def choose(self, node):
        if node.state.isGoalState():

            self.logger.log("Attempting to choose on a terminal state, returning None")

            return None

        if node not in self.children:
            child = node.state.findRandomChild()

            self.logger.log("Attempting to choose on an unexplored state, returning random next city: ", child[0].currentCity)

            return Node(child[0], node.getDirections() + [child[0].currentCity], node.getCost() + child[1])

        def score(node):
            if (self.counts[node] == 0):
                return float("-inf")
            return self.rewards[node] / self.counts[node]

        maxNode = max(self.children[node], key=score)
        
        self.logger.log("City ", maxNode.getCurrentState().currentCity, " has maximum score:", score(maxNode))
        
        return maxNode

    def doRollout(self, node):
        self.logger.log("Reward before rollout: ", self.rewards[node])
        self.logger.log("Count before rollout: ", self.counts[node])

        path = self.select(node)
        leaf = path[-1]
        self.expand(leaf)
        reward = self.simulate(leaf)
        self.backpropagate(path, reward)

        self.logger.log("Reward after rollout: ", self.rewards[node])
        self.logger.log("Count after rollout: ", self.counts[node])

    def select(self, node):
        path = []
        while True:
            path.append(node)
            if node not in self.children or not self.children[node]:
                return path
            
            unexploredStates = self.children[node] - self.children.keys()
            if unexploredStates:
                path.append(unexploredStates.pop())
                return path

            node = self.uctSelect(node)

    def uctSelect(self, node):

        assert all(n in self.children for n in self.children[node])

        log_N_vertex = log(self.counts[node])

        def uct(n):
            return self.rewards[n] / self.counts[n] + self.expWeight * sqrt(
                log_N_vertex / self.counts[n]
            )

        return max(self.children[node], key=uct)

    def expand(self, node):
        if node in self.children:
            return  
        self.children[node] = [Node(s[0], node.getDirections() + [s[1]], node.getCost() + s[2]) for s in node.state.nextStates()]

    def simulate(self, node):
        while True:
            if node.state.isGoalState():
                reward = 10/node.getCost()
                return reward

            child = node.state.findRandomChild()
            stepCost = child[1]
            node = Node(child[0], node.getDirections() + [child[0].currentCity], node.getCost() + stepCost)

    def backpropagate(self, path, reward):
        for node in reversed(path):
            self.counts[node] += 1
            self.rewards[node] += reward