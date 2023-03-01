class LinearQueue():

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None]*capacity
        self.tail = -1
        self.head = 0

    def enqueue(self, item):
        self.tail += 1
        self.queue[self.tail] = item

    def dequeue(self):
        if self.is_empty():
            print("Error: queue is empty.")
            quit()
        self.queue[self.head] = None
        self.head += 1

    def front(self):
        if self.is_empty():
            print("Error: queue is empty.")
            quit()
        return(self.queue[self.head])
    
    def back(self):
        if self.is_empty():
            print("Error: queue is empty.")
            quit()
        return(self.queue[self.tail])
    
    def is_empty(self):
        if self.queue[self.head] == None:
            return(True)
        else:
            return(False)
        
    def empty_queue(self):
        while True:
            if self.is_empty():
                self.head = 0
                self.tail = -1
                break
            else:
                self.dequeue()

    def reset_queue(self):
        tempHead = 0
        while True:
            if self.head == self.tail:
                self.queue[tempHead] = self.queue[self.head]
                self.queue[self.head] = None
                self.head = 0
                self.tail = -1
                break
            self.queue[tempHead] = self.queue[self.head]
            self.queue[self.head] = None
            tempHead += 1
            self.head += 1



q = LinearQueue(10)
#q.enqueue("Hello World")
#q.enqueue("Hola World")
#print(q.queue)
#q.enqueue("Wolrd innit")
#print(q.queue)
#q.dequeue()
#print(q.queue)
#print(q.front())
#print(q.is_empty())
#q.dequeue()
#q.dequeue()
#print(q.is_empty())
#q.enqueue("a")
#q.enqueue("b")
#print(q.queue)
#print(q.back())
#q.empty_queue()
#print(q.queue)
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
q.dequeue()
print(q.queue)
q.reset_queue()
print(q.queue)
# delete empty and test
q.empty_queue()
print("")

q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
q.enqueue("d")
q.enqueue("e")
q.dequeue()
q.dequeue()
print(q.queue)
q.reset_queue()
print(q.queue)
print("Has not quit.")