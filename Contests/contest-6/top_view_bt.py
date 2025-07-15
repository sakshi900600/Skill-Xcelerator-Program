class Queue():
    def __init__(self,cap):
        self.capacity = cap
        self.front = -1
        self.rear = -1
        self.cont = [0] * cap
    

    def add(self,data):
        if self.rear >= self.capacity-1:
            return 
        
        if self.rear == -1:
            self.front = 0
            self.rear = 0
            self.cont[self.rear] = data
            return

        self.rear += 1
        self.cont[self.rear] = data
        
    
    def remove(self):
        if self.front < 0:
            return -1
        
        data = self.cont[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
        return data
    

    def peek(self):
        if self.front < 0:
            return
        
        return self.cont[self.front]

    def is_empty(self):
        return self.front < 0
    
    


# q = Queue(1000)

# q.add(1)
# q.add(2)
# q.add(3)
# q.add(4)   

# while not q.is_empty():
    # print(q.remove())



# ques start ------------------------


dct = {
    "0" : 1,
    "-1" : 2,
    "1" : 3,
    "-2" : 4,
    "2" : 7
}

print(sorted(dct))
        
