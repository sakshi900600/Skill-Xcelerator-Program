# 10. Longest Increasing Subsequence 
# Problem: 
#  Find the length of the longest strictly increasing subsequence in an array. 
# Input: 
nums = [10, 9, 2, 5, 3, 7, 101, 18] 
# Output: 
#  4  (2,3,7,101).....


dp = [1] * len(nums)

for i in range(len(nums)):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


