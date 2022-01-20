from enum import *
from typing import *
import networkx as nx
import matplotlib.pyplot as plt


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    def __init__(self, data: Any, index):
        self.data = data
        self.index = index

    def __repr__(self):
        return f'{self.index}: {self.data}'


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies = {}

    def __str__(self, str=""):
        for source in self.adjacencies:
            for destination in self.adjacencies[source]:
                if destination not in self.adjacencies[source]:
                    self.adjacencies[source].append(destination)
                if source not in self.adjacencies[destination]:
                    self.adjacencies[destination].append(source)
        for data in self.adjacencies:
            str += f'{data} ----> {self.adjacencies[data]}\n'
        return str

    def create_vertex(self, value):
        vertex = Vertex(value, len(self.adjacencies))
        self.adjacencies[vertex] = []

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        edge = Edge(source, destination, weight)
        self.adjacencies[edge.source].append(edge.destination)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        edge = Edge(source, destination, weight)
        if edge.destination not in self.adjacencies[edge.source]:
            self.adjacencies[source].append(edge.destination)
        if edge.source not in self.adjacencies[edge.destination]:
            self.adjacencies[destination].append(edge.source)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        if edge == 1:
            self.add_directed_edge(source, destination, weight)
        elif edge == 2:
            self.add_undirected_edge(source, destination, weight)
        else:
            raise ValueError('Podano zla wartosc "edge"')

    def dfs(self, v: Vertex, visited: List[Vertex], visit: Callable[[Any], None]):
        visit(v)
        visited.append(v)
        for neighbour in self.adjacencies[v]:
            if neighbour.destination not in visited:
                self.dfs(neighbour.destination, visited, visit)

    def traverse_depth_first(self, visit: Callable[[Any], None]):
        visited = []
        v = list(graph1.adjacencies.keys())
        print(v)
        self.dfs(v[0], visited, visit)

    def show(self):
        draw = nx.DiGraph()
        options = {"edgecolors": "black", "node_size": 1750, "node_color": "lightblue", "arrows": True}
        edge = []
        for source in self.adjacencies:
            for destination in self.adjacencies[source]:
                edge.append((source, destination))
                draw.add_edges_from(edge)
        pos = nx.circular_layout(draw)
        nx.draw(draw, pos, **options, with_labels=True)
        plt.show()


def mutual_friends(g: Graph, f0: Any, f1: Any) -> List[Any]:
    mutual_list = []
    for value in g.adjacencies:
        if f0 in g.adjacencies[value] and f1 in g.adjacencies[value]:
            mutual_list.append(value)
    print("Dla wierzcholkow", f0, "oraz", f1, "wspolnymi znajomymi sa: ")
    return mutual_list


graph1 = Graph()

graph1.create_vertex("VI")  # 0
graph1.create_vertex("RU")  # 1
graph1.create_vertex("PA")  # 2
graph1.create_vertex("CO")  # 3
graph1.create_vertex("CH")  # 4
graph1.create_vertex("RA")  # 5
graph1.create_vertex("SU")  # 6
graph1.create_vertex("KE")  # 7


vertex = list(graph1.adjacencies.keys())

graph1.add(2, vertex[0], vertex[4])
graph1.add(2, vertex[0], vertex[1])
graph1.add(2, vertex[0], vertex[2])
graph1.add(2, vertex[1], vertex[5])
graph1.add(2, vertex[1], vertex[6])
graph1.add(2, vertex[1], vertex[0])
graph1.add(2, vertex[2], vertex[3])
graph1.add(2, vertex[2], vertex[7])
graph1.add(2, vertex[3], vertex[1])
graph1.add(2, vertex[3], vertex[0])


# print(mutual_friends(graph1, vertex[1], vertex[3]))
# graph1.show()
# print(graph1)


graph2 = Graph()

graph2.create_vertex("v0")
graph2.create_vertex("v1")
graph2.create_vertex("v2")
graph2.create_vertex("v3")
graph2.create_vertex("v4")
graph2.create_vertex("v5")

vertex = list(graph2.adjacencies.keys())

graph2.add_undirected_edge(vertex[0], vertex[1])
graph2.add_undirected_edge(vertex[0], vertex[5])
graph2.add_undirected_edge(vertex[2], vertex[1])
graph2.add_undirected_edge(vertex[2], vertex[3])
graph2.add_undirected_edge(vertex[3], vertex[4])
graph2.add_undirected_edge(vertex[4], vertex[1])
graph2.add_undirected_edge(vertex[4], vertex[5])
graph2.add_undirected_edge(vertex[5], vertex[1])
graph2.add_undirected_edge(vertex[5], vertex[2])


# print(mutual_friends(graph2, vertex[2], vertex[4]))
# graph2.show()
# print('\n\n', graph2)


graph3 = Graph()

graph3.create_vertex("AA")
graph3.create_vertex("BB")
graph3.create_vertex("CC")
graph3.create_vertex("DD")
graph3.create_vertex("EE")
graph3.create_vertex("FF")
graph3.create_vertex("GG")
graph3.create_vertex("HH")
graph3.create_vertex("II")

vertex = list(graph3.adjacencies.keys())

graph3.add(2, vertex[0], vertex[1])
graph3.add(2, vertex[0], vertex[3])
graph3.add(2, vertex[0], vertex[6])
graph3.add(2, vertex[1], vertex[7])
graph3.add(2, vertex[1], vertex[3])
graph3.add(2, vertex[1], vertex[2])
graph3.add(2, vertex[1], vertex[6])
graph3.add(2, vertex[2], vertex[6])
graph3.add(2, vertex[2], vertex[4])
graph3.add(2, vertex[2], vertex[1])
graph3.add(2, vertex[3], vertex[0])
graph3.add(2, vertex[3], vertex[5])
graph3.add(2, vertex[4], vertex[3])
graph3.add(2, vertex[4], vertex[2])
graph3.add(2, vertex[5], vertex[1])
graph3.add(2, vertex[6], vertex[1])
graph3.add(2, vertex[6], vertex[8])
graph3.add(2, vertex[6], vertex[3])
graph3.add(2, vertex[7], vertex[2])
graph3.add(2, vertex[7], vertex[1])
graph3.add(2, vertex[8], vertex[2])


print(mutual_friends(graph3, vertex[0], vertex[1]))
graph3.show()
print('\n\n', graph3)
