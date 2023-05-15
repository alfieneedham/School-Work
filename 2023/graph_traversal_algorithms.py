from abstract_data_types import CircularQueue, NaivePriorityQueue
from math import inf

time = 0

def input_edge(vertexOne, vertexTwo, type):
    # type == 1: directional graph. type == 2: non-directional graph.
    vertexOne.neighbours.append(vertexTwo)
    if type == 2:
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
    for vertex in graph:
        if vertex.entryTime == None:
            depth_visit(vertex)

def breadth_first_traversal(graph, start, destination):
    maze = {}
    path = []
    q = CircularQueue(len(graph))
    visitedVerteces = []
    
    q.enqueue(start)
    visitedVerteces.append(start)
    while q.is_empty() == False:
        currentVertex = q.dequeue()
        for neighbour in currentVertex.neighbours:
            if neighbour not in visitedVerteces:
                maze[neighbour] = currentVertex
                q.enqueue(neighbour)
                visitedVerteces.append(neighbour)
                
    path.append(destination)
    currentVertex = destination
    while currentVertex != start:
        try:
            path.append(maze[currentVertex])
            currentVertex = maze[currentVertex]
        except:
            print("No valid path.")
            quit()
            
    reversedPath = reversed(path)
    for vertex in reversedPath:
        print(vertex.name)
    return(reversedPath)
          
def sort_neighbours(vertex):
    for passes in range(len(vertex.neighbours)):
        madeSwap = False
        for comparisons in range(len(vertex.neighbours)-passes-1):
            if vertex.neighbours[comparisons].name > vertex.neighbours[comparisons+1].name:
                madeSwap = True
                vertex.neighbours[comparisons], vertex.neighbours[comparisons+1] = vertex.neighbours[comparisons+1], vertex.neighbours[comparisons]
        if madeSwap == False:
            break

if __name__ == "__main__":
    
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

    p = [a,b,c,d,e,f,g,h,i,j]
    
    input_edge(a,b,1)
    input_edge(a,c,1)
    input_edge(c,b,1)
    input_edge(c,j,1)
    input_edge(c,d,1)
    input_edge(d,e,1)
    input_edge(e,f,1)
    input_edge(d,f,1)
    input_edge(g,d,1)
    input_edge(g,f,1)
    input_edge(g,h,1)
    input_edge(g,i,1)

    for vertex in p:
        sort_neighbours(vertex)

    # depth_first_traversal(p)
    # print(a.entryTime, a.exitTime)
    # print(b.entryTime, b.exitTime)
    
    breadth_first_traversal(p, g, e)