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
    


class HeapPriorityQueue(PriorityQueue):
    
    def __init__(self):
        super().__init__()

    def enqueue(self, item, priority):
        super().enqueue(item, priority)
        print("Extra done.")




# q = LinearQueue(3)
# q.enqueue("a")
# print(q.get_queue())
# q.enqueue("b")
# print(q.get_queue())
# (q.dequeue())
# q.enqueue("c")
# print(q.get_queue())
# q.autoReset = True
# # q.enqueue("d")
# # print(q.get_queue())
# # q.enqueue("e")



# q = CircularQueue(6)
# q.enqueue(3)
# q.enqueue(7)
# q.enqueue(4)
# q.dequeue()
# q.enqueue(5)
# q.dequeue()
# q.enqueue(6)
# q.enqueue(2)
# q.dequeue()
# q.enqueue(9)
# q.dequeue()
# q.enqueue(8)
# q.dequeue()
# q.dequeue()
# print(q.get_queue())
# print(q.get_head())
# print(q.get_tail())   
 
 
 
# q = NaivePriorityQueue()
# q.enqueue("a", 21)
# print(q.get_queue())
# q.enqueue("b", 27)
# print(q.queue)
# print(q.queue[1][0])
# q.enqueue("c", 15)
# q.enqueue("d", 12)
# q.enqueue("e", 11)
# print(q.dequeue()[0])
# print(q.get_queue())

q = HeapPriorityQueue
q.enqueue("a", 1)