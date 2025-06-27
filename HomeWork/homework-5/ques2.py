# Given an array cost where cost[i] is the cost of step i, return the minimum cost to reach the top. You can climb either 1 or 2 steps. 

# Input:  cost = [10, 15, 20] 
# Output: 15

cost = [10,15,20]
n = len(cost)

li = [0]*len(cost)
li[0] = 0
li[1] = abs(cost[0]-cost[1])

for i in range(2,n):
    step1 = ljj