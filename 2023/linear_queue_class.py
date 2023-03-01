class LinearQueue():

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = [None]*capacity
        self.__tail = -1
        self.__head = 0
        self.autoReset = False

    def enqueue(self, item):
        try:
            self.__tail += 1
            self.__queue[self.__tail] = item
        except:
            self.__tail -= 1
            if self.autoReset and self.__head != 0:
                self.reset_queue()
                self.enqueue(item)

            else:
                print("Error: reached queue capacity. self.autoReset =", self.autoReset)
                quit()

    def dequeue(self):
        if self.is_empty():
            print("Error: queue is empty.")
            quit()
        itemToReturn = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head += 1
        return(itemToReturn)

    def front(self):
        if self.is_empty():
            print("Error: queue is empty.")
            quit()
        return(self.__queue[self.__head])
    
    def back(self):
        if self.is_empty():
            print("Error: queue is empty.")
            quit()
        return(self.__queue[self.__tail])
    
    def is_empty(self):
        if self.__queue[self.__head] == None:
            return(True)
        else:
            return(False)
        
    def empty_queue(self):
        while True:
            if self.is_empty():
                self.__head = 0
                self.__tail = -1
                break
            else:
                self.dequeue()

    def reset_queue(self):
        tempHead = 0
        while True:
            if self.__head == self.__tail:
                self.__queue[tempHead] = self.__queue[self.__head]
                self.__queue[self.__head] = None
                self.__head = 0
                self.__tail = tempHead
                break
            self.__queue[tempHead] = self.__queue[self.__head]
            self.__queue[self.__head] = None
            tempHead += 1
            self.__head += 1

    def get_queue(self):
        return(self.__queue)
    
    def get_capacity(self):
        return(self.__capacity)
    
    def get_head(self):
        return(self.__head)
    
    def get_tail(self):
        return(self.__tail)



q = LinearQueue(3)
q.enqueue("a")
print(q.get_queue())
q.enqueue("b")
print(q.get_queue())
(q.dequeue())
q.enqueue("c")
print(q.get_queue())
q.autoReset = True
q.enqueue("d")
print(q.get_queue())
q.enqueue("e")