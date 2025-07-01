# Jump Game - 2

# Find the minimum number of jumps to reach the end of the array.  
 
 
# Input: 
#  nums = [2, 3, 1, 1, 4] 
# Output: 
#  2


nums = [2, 3, 1, 1, 4] 
n = len(nums)
# li[i] = minimum no of jumps to reach at that index i

li = [0]*n

li[0] = 0

for i in range(2,n):
    li[i] = min(li[i-1]+1, li[i-2]+1)

print(li)
print(li[n-1])