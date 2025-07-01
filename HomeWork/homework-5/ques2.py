# Given an array cost where cost[i] is the cost of step i, return the minimum cost to reach the top. You can climb either 1 or 2 steps. 

# Input:  cost = [10, 15, 20] 
# Output: 10

cost = [10,15,20]
n = len(cost)

li = [0]*len(cost)
li[0] = 0
li[1] = abs(cost[0]-cost[1])

for i in range(2,n):
    step1 = li[i-1] + abs(cost[i-1] - cost[i])
    step2 = li[i-2] + abs(cost[i-2] - cost[i])
    li[i] = min(step1,step2)


print(li[n-1])