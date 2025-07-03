# 4. Reverse a Queue 
# Description: Reverse the elements of a queue using a stack. 
# Input: 
q = [1, 2, 3, 4, 5] 
 
# Output: 
# [5, 4, 3, 2, 1]

stack = []

def push(elem):
    stack.append(elem)

def pop():
    if len(stack) == 0:
        return "Stack is empty"
    removed_elem = stack.pop()
    return removed_elem

def peek():
    if len(stack) == 0:
        return "Stack is empty"
    return stack[-1]

def is_empty():
    return len(stack) == 0


for i in q:
    push(i)


i = 0
while not is_empty():
    q[i] = pop()
    i += 1


print(q)