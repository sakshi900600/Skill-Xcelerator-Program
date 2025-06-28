class Stack:
    def __init__(self, stack_cap):
        self.capacity = stack_cap
        self.top = -1
        self.container = [0]*stack_cap

    def push(self,x):
        if self.top >= self.capacity-1:
            print("Stack overflow")
            return False
        self.top += 1
        self.container[self.top] = x
        return True
    
    def pop(self):
        if self.top < 0:
            print("Stack underflow")
            return 0
        popped_elem = self.container[self.top]
        self.top -= 1
        return popped_elem
    
    def peek(self):
        if self.top < 0:
            print("Stack is empty")
            return 0
        return self.container[self.top]

    def is_empty(self):
        return self.top < 0
    
    def is_full(self):
        return self.top >= self.capacity-1
    

s = Stack(5)
s.pop()
s.push(10)
s.push(20)
s.push(30)
print(s.is_full())
print(s.is_empty())

while not s.is_empty():
    print(s.peek())
    s.pop()
