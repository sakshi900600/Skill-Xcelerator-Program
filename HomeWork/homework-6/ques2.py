# 2. Balanced Parentheses 
# Description: Given a string with brackets, check if it is balanced. 
# Input: 

s = "{[()([)]}" 
 
# Output: 
# False


# without using stack ---------
def isValid(s):
    for i in range(len(s)):
        if '()' or '{}' or '[]' in s:
            s = s.replace('()', "")
            s = s.replace('{}', "")
            s = s.replace('[]', "")


    if len(s) == 0:
        print("True")
    else:
        print("False")


# using stack  -----------------

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


for i in s:
    if i=='(' or i=='{' or i=='[' :
        push(i)

    elif (i==')' and peek()=='(') or (i=='}' and peek()=='{') or (i==']' and peek()=='['):
        pop()


if is_empty():
    print("Valid")
else: 
    print("Not valid")

