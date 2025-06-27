# Problem: 
# You are climbing a staircase. It takes n steps to reach the top. You can climb either 1 step or 2 steps at a time.  Count how many distinct ways you can climb to the top. 


# Input:  n = 5 
# Output:  8


n = 5
ways = [0] * n
ways[0] = 1 # 1 way to reach 1st stair (1)
ways[1] = 2 # 2 way to reach 2nd stair (1,1)(2)


for i in range(2,n):
    ways[i] = ways[i-1] + ways[i-2]


print(ways[n-1])
