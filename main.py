from enum import Enum
from typing import *


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    def __init__(self, data, index):
        self.data = data  # wartosc przechowywana w grafie
        self.index = index  # numer pozycji na liscie sasiedztwa


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

    def __init__(self, adjacencies=None):
        if adjacencies is None:
            adjacencies = {}
        self.adjacencies = adjacencies

    def create_vertex(self, data):
        vertex = Vertex(data, len(self.adjacencies))
        self.adjacencies[vertex] = []

    def add_directed_edge(self, source, destination, weight: Optional[float] = None):
        new_dir_edge = Edge(source, destination, weight)
        self.adjacencies[source].append(new_dir_edge)
        self.adjacencies[destination].append(new_dir_edge)

    def add_undirected_edge(self, source, destination, weight: Optional[float] = None):
        new_undir_edge = Edge(source, destination, weight)
        self.adjacencies[source].append(new_undir_edge)
        self.adjacencies[destination].append(new_undir_edge)

    def add(self, edge, source, destination, weight: Optional[float] = None):
        if edge == 1:
            self.add_directed_edge(source, destination, weight)
        if edge == 2:
            self.add_undirected_edge(source, destination, weight)

    def __str__(self, list=""):
        for key, value in self.adjacencies.items():
            list += f'- {key.index}: {key.data} ----> {Edge.destination.data}\n'
        return list


graph = Graph()

graph.create_vertex("v0")
graph.create_vertex("v1")
graph.create_vertex("v2")
graph.create_vertex("v3")
graph.create_vertex("v4")
graph.create_vertex("v5")

vertex = list(graph.adjacencies.keys())

graph.add_directed_edge(vertex[0], vertex[1])
graph.add_directed_edge(vertex[0], vertex[5])
graph.add_directed_edge(vertex[2], vertex[1])
graph.add_directed_edge(vertex[2], vertex[3])
graph.add_directed_edge(vertex[3], vertex[4])
graph.add_directed_edge(vertex[4], vertex[1])
graph.add_directed_edge(vertex[4], vertex[5])
graph.add_directed_edge(vertex[5], vertex[2])

print(Edge.destination.data)
# print(graph)
