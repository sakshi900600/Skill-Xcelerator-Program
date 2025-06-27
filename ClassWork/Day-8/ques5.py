# climb stairs with 1 or 2 steps

# 

# n = 4

# li = [0] * n

# li[0], li[1] = 1,2

# for i in range(2,n):
#     num = li[i-1] + li[i-2] 
#     li[i] = num


# # print(li)

# print(li[n-1])




# have 3 ways  
n = 4
li = [0] * n

li[0], li[1],li[2] = 1,2,4

for i in range(3,n):
    num = li[i-1] + li[i-2] + li[i-3]
    li[i] = num

# print(li)
# print(li[n-1])