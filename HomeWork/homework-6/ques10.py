#  10. Queue with Get Min() in O(1)



from collections import deque

class MinQueue():
    def __init__(self):
        self.allelem_queue = deque()
        self.min_queue = deque()

    
    def enqueue(self,x):
        self.allelem_queue.append(x)

        # getting min
        while self.min_queue and self.min_queue[-1] > x:
            self.min_queue.pop()
        self.min_queue.append(x)
    
    def dequeue(self):
        if not self.allelem_queue:
            return None
        
        x = self.allelem_queue.popleft()

        if x == self.min_queue[0]:
            self.min_queue.popleft()
        
        return x


    def getMin(self):
        if not self.min_queue:
            return None 
        
        return self.min_queue[0]


    def front(self): # peek()
        if not self.allelem_queue:
            return None
        
        return self.allelem_queue[0]
    
    
    def is_empty(self):
        return len(self.allelem_queue) == 0



q = MinQueue()
q.enqueue(3) 
q.enqueue(1) 
q.enqueue(2) 
print(q.getMin())
q.dequeue() 
print(q.getMin())  # 1 
q.dequeue() 
print(q.getMin())  # 2 
