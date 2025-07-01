# 💻 6. Jump Game I 
# Problem: 
#  Given an array nums, where each element represents your max jump from that position, determine if 
# you can reach the end. 
# Input: 
#  nums = [2, 3, 1, 1, 4] 
# Output: 
#  True


# li[i] = max index we can reach from the index i.

# nums = [2, 0, 1, 0, 4]  # false
nums = [2, 3, 1, 1, 4] # true

def jump_game1(nums):
    n = len(nums)
    if n == 1:
        return True
    
    li = [0] * n

    for i in range(0,n-1):
        li[i] = i + nums[i]
        if li[i] >= n-1:
            return True
    
    print(li)
    return False
    

print(jump_game1(nums))


