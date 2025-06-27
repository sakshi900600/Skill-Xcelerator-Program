# find out sum from index1 to index2

# inp = [2,9,8,1,5,7]
# n,m = 1,3

# typical way:
# sum = 0
# for i in range(n,m+1):
#     sum += inp[i]
# print(sum)




inp = [2,9,8,1,5,7]
n,m = 2,5

sum = [0] * len(inp)
sum[0] = inp[0]

for i in range(1,len(inp)):
    sum[i] = inp[i] + sum[i-1]

# print(sum)

# so sum from index n to m:
sum_nm = sum[m] - sum[n-1]
print(sum_nm)