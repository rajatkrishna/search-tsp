import plotly.offline as pyo
import plotly.graph_objects as go
from igraph import Graph, EdgeSeq
import itertools as it

class SearchTreeGenerator:

    def __init__(self, printGraph : bool, title : str):
        self.printGraph = printGraph
        if self.printGraph:
            self.title = title
            self.figure = go.Figure()
            self.vertices = set()
            self.edges = list()
            self.rootNode = None

    def addNode(self, node, parentNode = None):
        if self.printGraph:
            self.vertices.add(node)
            if not parentNode:
                self.rootNode = node
            else:
                self.edges.append([str(node), str(parentNode)])
                self.vertices.add(parentNode)

    def generate(self):
        if not self.printGraph:
            return
        
        vertexList = list(self.vertices)

        graph = Graph()
        graph.add_vertices([str(vertex) for vertex in vertexList])
        graph.add_edges(self.edges)

        if not self.rootNode:
            print("Failed to generate graph: No rootNode found!")
            return

        layout = graph.layout_reingold_tilford(mode = "in", root = [vertexList.index(self.rootNode)])
        position = {v: layout[v] for v in range(len(vertexList))}
        Y = [layout[v][1] for v in range(len(vertexList))]
        M = max(Y)

        es = EdgeSeq(graph)
        edges = [e.tuple for e in graph.es]

        Xn = [position[k][0] for k in range(len(position))]
        Yn = [2*M-position[k][1] for k in range(len(position))]

        hoverText = [self.formatHoverText(vertex.getDirections(), vertex.getCost()) for vertex in vertexList]

        Xe = []
        Ye = []

        for edge in edges:
            Xe += [position[edge[0]][0], position[edge[1]][0], None]
            Ye += [2 * M - position[edge[0]][1], 2 * M - position[edge[1]][1], None]

        self.figure.add_trace(go.Scatter(x=Xe,
                        y=Ye,
                        mode='lines',
                        line=dict(color='rgb(210,210,210)', width=1),
                        hoverinfo='none'
                        ))
        self.figure.add_trace(go.Scatter(x = Xn,
                        y = Yn,
                        mode = 'markers',
                        name = 'node',
                        marker = dict(symbol = 'circle-dot',
                                        size = 20,
                                        color = '#8da3a8',
                                        line = dict(color = 'rgb(50,50,50)', width = 1)
                                        ),
                        hoverinfo = 'text',
                        hovertext = hoverText,
                        opacity = 0.8
                        ))

        self.figure.update_layout(title = self.title,
              font_size = 12,
              showlegend = False,
              margin = dict(l=40, r=40, b=85, t=100),
              hovermode = 'closest',
              plot_bgcolor = 'rgb(230,230,230)'
              )
        self.figure.update_xaxes(visible = False)
        self.figure.update_yaxes(visible = False)

        self.figure.write_html('graph.html', auto_open=True)

    def formatHoverText(self, directions: list, cost: float):
        currentCity = directions[-1]
        response = ""

        response += "Current City ({})\tDirections ({})\tCost ({})".format(currentCity, directions, round(cost, 5))

        return response
