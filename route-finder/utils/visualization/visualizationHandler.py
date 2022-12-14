from utils.visualization.visualizationType import VisualizationType
from utils.node import Node
from utils.visualization.searchTreeGenerator import SearchTreeGenerator

class VisualizationHandler:

    def __init__(self):
        self.generators = dict()

    def initSearchTreeGenerator(self, title : str, printGraph : bool):
        self.generators[VisualizationType.ST_GENERATOR.value] = SearchTreeGenerator(printGraph, title)

    def addSearchTreeRootNode(self, node : Node):
        self.addSearchTreeNode(node, None)
        
    def addSearchTreeNode(self, node : Node, parentNode : Node):
        if not VisualizationType.ST_GENERATOR.value in self.generators:
            self.generators[VisualizationType.ST_GENERATOR.value] = SearchTreeGenerator(True, "Search Tree")

        self.generators[VisualizationType.ST_GENERATOR.value].addNode(node, parentNode)

    def generateSearchTree(self):  
        if not VisualizationType.ST_GENERATOR.value in self.generators:
            print("No search tree graph generator set")
            return

        self.generators[VisualizationType.ST_GENERATOR.value].generate()
