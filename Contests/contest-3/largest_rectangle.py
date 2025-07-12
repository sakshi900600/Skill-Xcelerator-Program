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