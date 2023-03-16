class Queue():
    def __init__(self, capacity):
        self._capacity = capacity
        self._queue = [None]*capacity
        self._tail = -1
        self._head = 0

    def empty_queue(self):
        while True:
            if self.is_empty():
                self._head = 0
                self._tail = -1
                break
            else:
                self.dequeue()

    def front(self):
        return(self._queue[self._head])
    
    def back(self):
        return(self._queue[self._tail])
    
    def is_empty(self):
        if self._queue[self._head] == None:
            return(True)
        else:
            return(False)

    def get_queue(self):
        return(self._queue)
    
    def get_capacity(self):
        return(self._capacity)
    
    def get_head(self):
        return(self._head)
    
    def get_tail(self):
        return(self._tail)



class LinearQueue(Queue):

    def __init__(self, capacity):
        super().__init__(capacity)
        self.autoReset = False

    def enqueue(self, item):
        try:
            self._tail += 1
            self._queue[self._tail] = item
        except:
            self._tail -= 1
            if self.autoReset and self._head != 0:
                self.reset_queue()
                self.enqueue(item)

            else:
                print("Error: reached queue capacity. self.autoReset =", self.autoReset)
                quit()

    def dequeue(self):
        if self.is_empty():
            print("Error: queue is empty.")
            quit()
        itemToReturn = self._queue[self._head]
        self._queue[self._head] = None
        self._head += 1
        return(itemToReturn)

    def reset_queue(self):
        tempHead = 0
        while True:
            if self._head == self._tail:
                self._queue[tempHead] = self._queue[self._head]
                self._queue[self._head] = None
                self._head = 0
                self._tail = tempHead
                break
            self._queue[tempHead] = self._queue[self._head]
            self._queue[self._head] = None
            tempHead += 1
            self._head += 1



class CircularQueue(Queue):

    def __init__(self, capacity):
        super().__init__(capacity)

    def enqueue(self, item):
        self._tail += 1
        if self._tail == self._capacity:
            self._tail = 0
        self._queue[self._tail] = item

    def dequeue(self):
        itemToReturn = self._queue[self._head]
        self._queue[self._head] = None
        self._head += 1
        if self._head == self._capacity:
            self._head = 0
        return(itemToReturn)



# * For both priority queues, the lower the value, the greater the priority.
# * For both priority queues, the maximum priority is 0.

class PriorityQueue():

    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        if priority < 0:
            print("Error: priority cannot be lower than 0.")
            quit()
        tupleToAppend = (item, priority)
        self.queue.append(tupleToAppend)
        print("Done")

class NaivePriorityQueue(PriorityQueue):

    def __init__(self):
        super().__init__()

    # * Returns both item and its priority as a tuple.
    def dequeue(self):
        greatestPriority = self.queue[0][1]
        indexOfGreatestPriority = 0
        for i in range(len(self.queue)):
            if self.queue[i][1] < greatestPriority:
                greatestPriority = self.queue[i][1]
                indexOfGreatestPriority = i
        itemToReturn = self.queue[indexOfGreatestPriority]
        self.queue.remove(self.queue[indexOfGreatestPriority])
        return(itemToReturn)

    def get_queue(self):
        return(self.queue)
    

# * FINISH por favor
class HeapPriorityQueue(PriorityQueue):
    
    def __init__(self):
        super().__init__()

    def enqueue(self, item, priority):
        super().enqueue(item, priority)
        print("Extra done.")
        
 
        
class Graph():

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.matrix = []
        self.list = []
        for i in range(vertices):
            self.matrix.append([0]*vertices)
            self.list.append([])
        for i in range(edges):
            self.input_edge()

    def input_edge(self):
        start, end = input("Enter edge [from:to]: ").split(":")
        self.matrix[int(start)][int(end)] = 1
        if int(end) not in self.list[int(start)]:
            self.list[int(start)].append(int(end))



class HashTable():

    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [[None,None,None]]*capacity
        self.emptySpaces = []
        self.top = capacity

    def insert(self, item):
        inserted = False
        spaceToInsert = item%self.capacity
        prevSpace = None

        while inserted == False:
            try:
                if self.table[spaceToInsert][0] == None:
                    self.table[spaceToInsert] = [item, None, prevSpace]
                    inserted = True
                else:
                    prevSpace = spaceToInsert
                    if self.table[spaceToInsert][1] == None:
                        spaceToInsert = self.top
                    else:
                        spaceToInsert = self.table[spaceToInsert][1]
            except:
                if len(self.emptySpaces) != 0:
                    self.table[self.emptySpaces[-1]] = [item, None, prevSpace]
                    self.table[prevSpace][1] = self.emptySpaces[-1]
                    self.emptySpaces.pop(-1)
                else:
                    self.table.append([item, None, prevSpace])
                    self.table[prevSpace][1] = spaceToInsert
                    self.top += 1
                inserted = True

    def remove(self, item):
        index = item%self.capacity
        while True:
            if (self.table[index][0]) == item:
                nextIndex = self.table[index][1]
                prevIndex = self.table[index][2]
                self.table[prevIndex][1] = self.table[index][1]
                if self.table[index][1] != None:
                    self.table[nextIndex][2] = self.table[index][2]
                self.table[index] = [None, None, None]
                self.emptySpaces.append(index)
                break
            else:
                index = self.table[index][1]

t = HashTable(20)
t.insert(37)
t.insert(91)
t.insert(22)
t.insert(51)
t.insert(82)
t.insert(31)
print("")
print(t.table)
print("")
t.remove(31)
print(t.table)
print("")
t.insert(31)
print(t.table)
print("")
t.insert(587)
t.insert(607)
print(t.table)

# g = Graph(5,2)
# print(g.matrix)
# print(g.list)