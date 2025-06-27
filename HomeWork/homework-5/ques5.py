
# Given an array, return the maximum sum of non-adjacent elements. 
# Input: arr = [3, 2, 5, 10, 7] 
# Output: 15


arr = [3, 2, 5, 10, 7]
n = len(arr)
li = [0]*n

li[0] = arr[0]
li[1] = max(arr[0],arr[1])

for i in range(2,n):
    li[i] = li[i-2]+ arr[i]
    i += 1

print(li[-1])