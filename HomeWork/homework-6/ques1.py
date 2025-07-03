# Implement a Stack Using List


stack = []

def push(elem):
    stack.append(elem)
    return 

def pop():
    if len(stack) == 0:
        return "Stack is empty"
    
    removed_elem = stack.pop()
    return removed_elem

def peek():
    if not stack:
        print("Stack is empty")
    
    return stack[-1]

def is_empty():
    return len(stack) == 0



print(pop())
push(10)
push(20)
push(30)
print(pop())
print(peek())
print(is_empty())
