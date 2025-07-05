# Next Greater Element 
# Description: For every element in the array, find the next greater element to its righ

arr = [4, 5, 2, 25,1,2] 
 
# Output: 
# [5, 25, 25, -1]

# li = [-1]* len(arr)

# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[j] > arr[i]:
#             li[i] = arr[j]
#             break

# print(li)





stack = []

def push(elem):
    stack.append(elem)

def pop():
    if len(stack) == 0:
        return -1
    removed_elem = stack.pop()
    return removed_elem

def peek():
    if len(stack) == 0:
        return -1
    return stack[-1]

def is_empty():
    return len(stack) == 0


# to loop opposite
# for i in range(len(arr)-1, -1,-1):
#     push(arr[i])


i = len(arr)-1
while i >=0 :
    push(arr[i])
    i -= 1

# print(peek())

ans = [-1] * len(arr)

for i in range(len(arr)):
    while not is_empty() and peek() <= arr[i]:
        pop()
    ans[i] = peek() 



print(ans)
