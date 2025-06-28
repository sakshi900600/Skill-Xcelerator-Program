# 3. House Robber 🏠 
# Problem: 
#  You are a robber. Each house has some money. You can’t rob two adjacent houses. Return the 
# maximum amount you can rob. 
# Input: 
#  nums = [2, 7, 9, 3, 1]
# ans = 12


nums = [2, 7, 9, 3, 1]
n = len(nums)
li = [0]*n

li[0] = 2
li[1] = max(li[0],li[1])

for i in range(2,n):
    rob = li[i-2] + nums[i]
    notrob = li[i-1] # max amount till last index if not robbing at current index

    li[i] = max(rob,notrob)


print(li[-1])
