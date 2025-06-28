class Queue:
    def __init__(self, queue_cap):
        self.capacity = queue_cap
        self.first = -1
        self.end = -1
        self.container = [0]*queue_cap
    
    def push(self,x):
        if self.end >= self.capacity-1:
            print("Queue overflow")
            return False

        if self.first == self.end:
            self.first += 1
            self.end += 1
            self.container[self.end] = x
            return True

        else:
            self.end += 1
            self.container[self.end] = x
            return True
            
    
    def pop(self):
        if self.end < 0:
            print("Queue is empty")
            return 0
        
        popped_elem = self.container[self.first % self.capacity]
        self.first += 1
        return popped_elem
    
    
    def peek(self):
        if self.end < 0:
            print("Queue is empty")
            return 0
        
        return self.container[self.first % self.capacity]
    

    
    def is_empty(self):
        return self.end < 0
    
    def is_full(self):
        return self.end >= self.capacity-1
    


q = Queue(5)
q.push(10)
q.push(20)
q.push(30)


while not q.is_empty():
    print(q.peek())
    q.pop()

    

        