# 1. Largest Rectangle in Histogram 
# Description: Given an array representing histogram bar heights, find the area of the largest rectangle. 
# Input: 
# heights = [2, 1, 5, 6, 2, 3] 
 
# Output: 
# 10


# logic: Stand at each index and find area from that index to nth and store max area in a variable.  And of course it may possible that somewhere height is min from current height so everytime check min height and then calculate area.


# a = [2, 1, 5, 6, 2, 3]
a = [1,2,3,4,5]

# tle
def brute_method(a):
    n = len(a)
    maxArea = 0

    for i in range(n):
        minh = a[i]
        for j in range(i,n):
            minh = min(minh, a[j])
            width = j-i+1
            area = minh * width
            maxArea = max(maxArea, area)


    print(maxArea)

# brute_method(a)


# in first method we are maintaining minh so that we can calculate correct area.
# So in next approach i will calculate and store next and previous smaller elem and then calculate area = a[i] * (nse-pse-1)(width)
# and of course for nse and pse we will store indexes. 


def nse(a):
    n = len(a)
    nse = [0] * n
    stack = []

    for i in range(n-1,-1,-1):
        while stack and a[i] <= a[stack[-1]]:
            stack.pop()
        
        if len(stack) != 0:
            nse[i] = stack[-1]
        else:
            nse[i] = n # coz if we do -1 then it can lead to -ve width.
        
        stack.append(i)
    
    return nse


def pse(a):
    n = len(a)
    pse = [0]*n
    stack = []

    for i in range(n):
        while stack and a[i] <= a[stack[-1]]:
            stack.pop()
        
        if stack:
            pse[i] = stack[-1]
        else:
            pse[i] = -1
        
        stack.append(i)
    
    return pse


# print(nse(a))
# print(pse(a))

def better(a):
    n = len(a)
    nse_elem = nse(a)
    pse_elem = pse(a)

    maxArea = 0

    for i in range(n):
        area = a[i] * (nse_elem[i]-pse_elem[i]-1)
        maxArea = max(maxArea, area)
    
    return maxArea


print(better(a))

