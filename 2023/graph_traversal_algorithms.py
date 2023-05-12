time = 0

def input_edge(vertexOne, vertexTwo, type):
    # type == 1: non-directed graph. type == 2: directed graph.
    vertexOne.neighbours.append(vertexTwo)
    if type == 1:
        vertexTwo.neighbours.append(vertexOne)

class Vertex():
    def __init__(self, name):
        self.name = name
        self.entryTime = None
        self.exitTime = None
        self.parent = None
        self.neighbours = []

def __depth_visit(vertex):
    global time
    time += 1
    vertex.entryTime = time
    for neighbour in vertex.neighbours:
        if neighbour.entryTime == None:
            neighbour.parent = vertex
            __depth_visit(neighbour)
    time += 1
    vertex.exitTime = time

def depth_first_traversal(graph):
    for vertex in graph:
        if vertex.entryTime == None:
            __depth_visit(vertex)

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

p = [a,b,c,d,e,f,g,h,i,j,k,l]

input_edge(a, b,1)
input_edge(e, b,1)
input_edge(e, f,1)
input_edge(a, c,1)
input_edge(c, d,1)
input_edge(d, f,1)
input_edge(d, g,1)
input_edge(g, h,1)
input_edge(g, i,1)
input_edge(i, j,1)
input_edge(i, k,1)
input_edge(i, l,1)
input_edge(k, l,1)

def sort_neighbours(vertex):
    for passes in range(len(vertex.neighbours)):
        madeSwap = False
        for comparisons in range(len(vertex.neighbours)-passes-1):
            if vertex.neighbours[comparisons].name > vertex.neighbours[comparisons+1].name:
                madeSwap = True
                vertex.neighbours[comparisons].name, vertex.neighbours[comparisons+1].name = vertex.neighbours[comparisons+1].name, vertex.neighbours[comparisons].name
        if madeSwap == False:
            break

for vertex in p:
    sort_neighbours(vertex)

depth_first_traversal(p)
print(a.entryTime, a.exitTime)