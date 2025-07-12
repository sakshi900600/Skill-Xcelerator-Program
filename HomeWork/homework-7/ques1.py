# 1. Largest Rectangle in Histogram 
# Description: Given an array representing histogram bar heights, find the area of the largest rectangle. 
# Input: 
# heights = [2, 1, 5, 6, 2, 3] 
 
# Output: 
# 10


# logic: Stand at each index and find area from that index to nth and store max area in a variable.  And of course it may possible that somewhere height is min from current height so everytime check min height and then calculate area.


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