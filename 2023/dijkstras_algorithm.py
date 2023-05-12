from abstract_data_types import NaivePriorityQueue
from math import inf

def input_edge(vertexOne, vertexTwo, weight):
    vertexOne.neighbours.append((vertexTwo, weight))

class Vertex():
    def __init__(self, name):
        self.name = name
        self.entryTime = None
        self.exitTime = None
        self.parent = None
        self.neighbours = []

def dijkstras_algorithm(graph, start, destination):

    def find_index(vertex):
        for i in range(len(vertices)):
            if vertices[i][0].name == vertex.name:
                return(i)

    queue = NaivePriorityQueue()
    vertices = []
    for vertex in graph:
        # tuple: (vertex, parent, distance to vertex)
        vertices.append([vertex, None, inf])

    vertices[find_index(start)][1] = start
    vertices[find_index(start)][2] = 0
    queue.enqueue(start, 0)

    while queue.is_empty():
        currentVertex = queue.dequeue
        for neighbour in currentVertex.neighbours:
            if vertices[find_index(currentVertex[0])][2] + neighbour[1] < vertices[find_index(neighbour[0])][2]:
                vertices[find_index(neighbour[0])][2] = vertices[find_index(currentVertex[0])][2] + neighbour[1]
                vertices[find_index(neighbour[0])][1] = currentVertex
                queue.enqueue(neighbour[0], vertices[find_index(currentVertex[0])][2] + neighbour[1])

    for vertex in vertices:
        try:
            print(vertex[0].name, vertex[1].name, vertex[2])
        except:
            print(vertex[0].name, vertex[1], vertex[2])
    


a = Vertex("a")
b = Vertex("b")
c = Vertex("c")
d = Vertex("d")
e = Vertex("e")
p = [a, b, c, d, e]

input_edge(a, b, 60)
input_edge(a, c, 200)
input_edge(a, d, 170)
input_edge(d, e, 210)
input_edge(b, c, 120)
input_edge(c, e, 100)
input_edge(b, e, 200)

dijkstras_algorithm(p, a, b)