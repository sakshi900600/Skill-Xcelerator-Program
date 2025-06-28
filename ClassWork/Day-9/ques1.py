# maximum subarray sum:

a = [2,-5,3,-2,2,4,-1]
n = len(a)

# dp = [0]*len(a)
# dp[0] = a[0]

# maxSum = a[0]
# for i in range(1,n):
#     dp[i] = max(a[i], dp[i-1]+a[i])
#     maxSum = max(maxSum, dp[i])

# print(maxSum)



# without using dp list

prev = a[0]
maxSum = a[0]

for i in range(1,n):
    curr = max(a[i],prev+a[i])
    prev = curr
    maxSum = max(maxSum, curr)

print(maxSum)