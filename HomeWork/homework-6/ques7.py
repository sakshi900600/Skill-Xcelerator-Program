#  7. Sliding Window Maximum (Queue-based) 
# Description: Given an array and a window size k, print the max of each subarray of size k. 
# Input: 
nums = [1,3,-1,-3,5,3,6,7] 
k = 3 
 
# Output: 
# [3, 3, 5, 5, 6, 7] 


# My approach:  I will take a queue and i iwll always maintain exactly k elem in queue and get max of all k elem and store it in answer and after storing i will pop one elem from it. ultimately we get our answer.



   

# 1 way -----------------
def slidwndomax(nums,k):
    n = len(nums)
    li = []

    for i in range(n-k+1):
        maxi = nums[i]

        for j in range(i, i+k):
            maxi = max(maxi, nums[j])
        li.append(maxi)

    print(li)

# slidwndomax(nums,k)



# 2 way ----------------
from collections import deque


def slidwndomax2(nums,k):
    n = len(nums)
    dq = deque()
    ans = []
    for i in range(n):
        if dq and dq[0] <= i-k:
            dq.popleft()
        
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)

        if i >= k-1:
            ans.append(nums[dq[0]])
    
    print(ans)


slidwndomax2(nums,k)




