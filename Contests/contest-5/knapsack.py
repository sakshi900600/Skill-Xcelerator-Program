def unboundedKnapsack(k, arr):
    # Write your code here
    n = len(arr)
    
    dp = [False] * (k+1)
    dp[0] = True
    
    for it in arr:
        for t in range(it,k+1):
            if dp[t-it] == True:
                dp[t] = True
                
    for i in range(k,-1,-1):
        if dp[i] == True:
            return i
        
    return 0


# dp[i] = whether i sum is possible or not.
# logic: store true/False in dp from 0 to k+1 and in order to get the closest one traverse it from back where you find true return. Otherwise return 0



# arr = [1,6,9] # 12
# k = 12

arr = [3,4,4,4,8]
k = 9


result = unboundedKnapsack(k, arr)
print(result)