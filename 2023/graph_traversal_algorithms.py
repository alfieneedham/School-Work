time = 0

class Graph():

    def __init__(self, vertices):
        self.list = []

    def input_vertex(self, vertex):
        self.list.append(vertex)

def input_edge(vertexOne, vertexTwo):
    vertexOne.neighbours.append(vertexTwo)
    vertexTwo.neighbours.append(vertexOne)

class Vertex():
    def __init__(self, name):
        self.name = name
        self.entryTime = None
        self.exitTime = None
        self.parent = None
        self.neighbours = []

def depth_visit(vertex):
    global time
    time += 1
    print(vertex.name)
    vertex.entryTime = time
    for neighbour in vertex.neighbours:
        if neighbour.entryTime == None:
            neighbour.parent = vertex
            depth_visit(neighbour)
        time += 1
        vertex.exitTime = time

def depth_first_traversal(graph):
    for vertex in graph.list:
        if vertex.entryTime == None:
            depth_visit(vertex)

p = Graph(7)
a = Vertex("a")
b = Vertex("b")
c = Vertex("c")
d = Vertex("d")
e = Vertex("e")
f = Vertex("f")
g = Vertex("g")
h = Vertex("h")
i = Vertex("i")
j = Vertex("j")
k = Vertex("k")
l = Vertex("l")

p.input_vertex(a)
p.input_vertex(b)
p.input_vertex(c)
p.input_vertex(d)
p.input_vertex(e)
p.input_vertex(f)
p.input_vertex(g)
p.input_vertex(h)
p.input_vertex(i)
p.input_vertex(j)
p.input_vertex(k)
p.input_vertex(l)

input_edge(a, b)
input_edge(e, b)
input_edge(e, f)
input_edge(a, c)
input_edge(c, d)
input_edge(d, f)
input_edge(d, g)
input_edge(g, h)
input_edge(g, i)
input_edge(i, j)
input_edge(i, k)
input_edge(i, l)


def print_neighbours(vertex):
    for neighbour in vertex.neighbours:
        print(neighbour.name)

depth_visit(a)
print(a.entryTime, a.exitTime)