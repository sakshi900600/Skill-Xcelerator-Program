# 6. Sort a Stack 
# Description: Sort the elements of a stack using another stack (no other data structures)

# Input: 
# stack = [34, 3, 31, 98, 92, 23] 
 
# Output: 
# [3, 23, 31, 34, 92, 98]


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
            return False
        popped_elem = self.container[self.top]
        self.top -= 1
        return popped_elem
    
    def peek(self):
        if self.top < 0:
            return False
        return self.container[self.top]

    def is_empty(self):
        return self.top < 0
    
    def is_full(self):
        return self.top >= self.capacity-1
    

# stack is ready
st = Stack(100)
# st.push(23)
# st.push(92)
# st.push(98)
# st.push(31)
# st.push(3)

# output: 1 2 3 4 
st.push(1)
st.push(2)
st.push(3)
st.push(4)

# while not st.is_empty():
#     print(st.pop(), end=" ")


# let's sort it: 
s2 = Stack(100)

while not st.is_empty():
    li = []
    curr_elem = st.peek()
    while curr_elem > s2.peek() and not s2.is_empty():
        li.append(s2.pop())
    
    s2.push(st.pop())

    while len(li) != 0:
        s2.push(li.pop())



while not s2.is_empty():
    print(s2.pop(), end=" ")