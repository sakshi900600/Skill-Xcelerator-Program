# Return the n-th Fibonacci number. 
# Input: n = 7 
# Output: 13 

li = [0]*100

n = 7

li[0], li[1] = 0,1

for i in range(2,100):
    li[i] = li[i-1] + li[i-2]

print(li[n])