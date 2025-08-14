def largestRectangle(h):
    # Write your code here
    n = len(h)
    maxArea = 0
    
    for i in range(n):
        minh = h[i]
        for j in range(i,n):
            minh = min(h[j], minh)
            width = j-i+1
            area = minh * width
            maxArea = max(area, maxArea)
    
    return maxArea


# the above approach gives TLE so need to optimize using stack.



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
