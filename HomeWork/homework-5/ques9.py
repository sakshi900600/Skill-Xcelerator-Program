# 9. Decode Ways 
# Problem: 
#  A message containing letters from A-Z is encoded with numbers '1' to '26'. Count the total number of 
# ways to decode it. 
# Input: 
# s = "226" 
# s = "06" 
s = "100" 
# Output: 
#  3 


# explaination:
# 226: 2,2,6  22,6  2,26  = 3 ways.


n = len(s)
dp = [0] * (len(s)+1)
dp[0] = 1
if s[0] != '0':
    dp[1] = 1
else:
    dp[1] = 0


for i in range(2, len(s)+1):
    if s[i-1] != '0':
        dp[i] += dp[i-1]
    
    if s[i-2] != '0' and 10 <= int(s[i-2:i]) <= 26:
        dp[i] += dp[i-2]


print(dp[n])