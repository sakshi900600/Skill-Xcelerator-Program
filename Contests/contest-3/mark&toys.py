# https://www.hackerrank.com/contests/cpu-skill-xcelerator-contest-3/challenges/mark-and-toys/submissions

# The logic is very simple. If you want to maximize toys then you will have to take toys with minimum cost. 

# and to take min cost toys first sort the array.


prices = [1,12,5,111,200,1000,10]
k = 50

def maximumToys(prices,k):
    prices = sorted(prices)
    toys = 0
    n = len(prices)
    for i in range(n):
        if prices[i] < k:
            toys += 1
            k -= prices[i]

    return toys


print(maximumToys(prices,k))