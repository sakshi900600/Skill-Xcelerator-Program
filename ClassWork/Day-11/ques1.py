# length of longest increasing substring of 2 strings

# we have used here 2D dp coz in 1D dp there were some problems and was not possible to handle some data properly.

# we are creating n+1,m+1 size dp so that we can handle case when any of string is empty. 

# if at any index char is same then only we are updating. 

# s1 = "AKLI"
# s2 = "HKLP"

s1 = "ABCDEF"
s2 = "GCDEHI"
n = len(s1)
m = len(s2)

dp = [[0]*(n+1) for i in range(m+1)]
longest = 0



for i in range(n+1):
    for j in range(m+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
            longest = max(dp[i][j], longest)



# print(dp)
print(longest)
