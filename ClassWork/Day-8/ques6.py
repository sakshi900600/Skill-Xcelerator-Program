# frog will jump either 1 or 2 elem and cost will be absolute difference of both indexes.


arr = [10, 30, 40, 20, 60, 10]
n = len(arr)
# output = 20

# li[i] means cost to reach at ith index. 
li = [0]*n
li[0] = 0
li[1] = abs(arr[1]-arr[0])

for i in range(2,n):
    # taking one step back to reach current index
    step1 = li[i-1] + abs(arr[i]-arr[i-1])
    step2 = li[i-2] + abs(arr[i]-arr[i-2])
    li[i] = min(step1,step2)

# print(li)
print(li[-1])