class Stack():

    def __init__(self,stack_cap):
        self.capacity =  stack_cap
        self.top = -1
        self.container = [0]*stack_cap

    def push(self,x):
        if self.top >= self.capacity:
            print("Stack Overflow")
            return False
        
        self.top += 1
        self.container[self.top] = x
        return True
    
    def pop(self):
        if self.top < 0:
            return "Stack UnderFlow"
        
        popped_elem = self.container[self.top]
        self.top -= 1
        return popped_elem
    
    def peek(self):
        if self.top < 0:
            return "Stack UnderFlow"
        return self.container[self.top]

    
    def is_empty(self):
        return self.top < 0

    def is_full(self):
        return self.top >= self.capacity

# s1 = Stack(7)
# s1.push(10)
# s1.push(20)
# s1.push(30)

# while not s1.is_empty():
#     print(s1.pop())



#  5. Implement a Queue Using Two Stacks 
# Description: Implement enqueue and dequeue using two stacks. 
# Input: 
# q = MyQueue() 
# q.enqueue(1) 
# q.enqueue(2) 
# q.enqueue(3) 
# print(q.dequeue()) 
# print(q.dequeue())


class MyQueue():
    def __init__(self,stack1, stack2):
        self.s1 = stack1
        self.s2 = stack2

    def enqueue(self,x):
        while not self.s1.is_empty():
            self.s2.push(self.s1.pop())
        self.s1.push(x)

        self.s2.push(self.s1.pop())

        while not self.s2.is_empty():
            self.s1.push(self.s2.pop())


    def dequeue(self):
        if self.s1.is_empty():
            return "empty"
        
        removed_elem = self.s1.pop()
        return removed_elem
        
    def top(self):
        if self.s1.is_empty():
            return "empty"
        
        return self.s1.peek()

    def isempty(self):
        return self.s1.is_empty()





s1 = Stack(100)
s2 = Stack(100)


q = MyQueue(s1,s2)

print(q.dequeue()) 
q.enqueue(1) 
q.enqueue(2) 
# q.enqueue(3) 
# print(q.top())
print(q.dequeue()) 
print(q.dequeue())
print(q.isempty())
