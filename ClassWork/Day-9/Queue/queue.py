class Queue:
    def __init__(self, queue_cap):
        self.capacity = queue_cap
        self.first = -1
        self.end = -1
        self.container = [0]*queue_cap
    
    
    def push(self,data):
        if self.end >= self.capacity-1:
            return
        
        if self.end == -1:
            self.end = 0
            self.first = 0
            self.container[self.end] = data
            return

        self.end += 1
        self.container[self.end] = data

    
    def pop(self):
        if self.first < 0:
            return
        
        data = self.container[self.first]

        if self.first == self.end:
            self.first = -1
            self.end = -1
        else:
            self.first += 1
        return data
        
    
    def peek(self):
        if self.is_empty():
            return
        
        return self.container[self.first]

    
    def is_empty(self):
        return self.first < 0
    
    def is_full(self):
        return self.end >= self.capacity-1
    


q = Queue(5)
q.push(10)
q.push(20)
q.push(30)
q.push(40)
q.push(50)
print(q.peek())
print(q.is_empty())
print(q.is_full())

# print(q.pop())
# print(q.pop())
# print(q.pop())

while not q.is_empty():
    print(q.peek(), end=" ")
    q.pop()

    

        