# 8. Evaluate Reverse Polish Notation (Postfix) 
# Description: Evaluate an expression given in postfix notation. 
# Input: 
tokens = ["2", "1", "+", "3", "*"] 
 
# Output: 
# 9
# print(tokens[0].isdigit())

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


for i in tokens:
    if i.isdigit():
        push(i)
    else:
        op = i
        elem1 = pop()
        elem2 = pop()
        res = eval(f"{elem2}{op}{elem1}")
        push(res)

print(peek())