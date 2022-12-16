from utils.visualization.visualizationType import VisualizationType
from utils.node import Node
from utils.visualization.searchTreeGenerator import SearchTreeGenerator
from utils.visualization.SearchStatusViewGenerator import SearchStatusViewGenerator

class VisualizationHandler:

    def __init__(self):
        self.generators = dict()

    def initSearchTreeGenerator(self, title : str, printGraph : bool):
        self.generators[VisualizationType.ST_GENERATOR.value] = SearchTreeGenerator(printGraph, title)

    def initSearchStatusViewGenerator(self, rate = 100):
        self.generators[VisualizationType.SSV_GENERATOR.value] = SearchStatusViewGenerator(rate)

    def addSearchTreeRootNode(self, node : Node):
        self.addSearchTreeNode(node, None)
        
    def addSearchTreeNode(self, node : Node, parentNode : Node):
        if not VisualizationType.ST_GENERATOR.value in self.generators:
            self.initSearchTreeGenerator("Search Tree", True)

        self.generators[VisualizationType.ST_GENERATOR.value].addNode(node, parentNode)

    def generateSearchTree(self):  
        if not VisualizationType.ST_GENERATOR.value in self.generators:
            print("No search tree graph generator set")
            return

        self.generators[VisualizationType.ST_GENERATOR.value].generate()

    def write(self, obj):
        if not VisualizationType.SSV_GENERATOR.value in self.generators:
            self.initSearchStatusViewGenerator()

        self.generators[VisualizationType.SSV_GENERATOR.value].write(obj)
        
