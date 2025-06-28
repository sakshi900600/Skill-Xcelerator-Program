
# Max Sum of Non-Adjacent Elements

# Given an array, return the maximum sum of non-adjacent elements. 
# Input: arr = [3, 2, 5, 10, 7] 
# Output: 15


# arr = [3, 2, 5, 10, 7]
arr = [5,5,10,100,10]
n = len(arr)
li = [0]*n

li[0] = arr[0]
li[1] = max(arr[0],arr[1])

for i in range(2,n):
    li[i] = max(li[i-1], li[i-2]+ arr[i])


print(li)
print(li[-1])