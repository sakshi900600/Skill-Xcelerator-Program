# 1. Largest Rectangle in Histogram 
# Description: Given an array representing histogram bar heights, find the area of the largest rectangle. 
# Input: 
# heights = [2, 1, 5, 6, 2, 3] 
 
# Output: 
# 10


a = [2, 1, 5, 6, 2, 3]

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