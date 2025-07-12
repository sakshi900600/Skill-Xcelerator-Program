# 8. coin change
# Problem: 
#  You are given coins of different denominations and a total amount. Find the minimum number of coins to make that amount. Return -1 if not possible. 
# Input: 
coins = [1, 2, 5]
amount = 11 
# Output: 
#  3


dp = [100]*(amount+1)
dp[0] = 0

for coin in coins:
    for i in range(coin, amount+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

print(dp[len(dp)-1])
