# def extraLongFactorials(n):
#     # Write your code here
#     if n==1:
#         return 1
    
#     return n * extraLongFactorials(n-1)


# n = 25

# print(extraLongFactorials(n))



# ques 2



s = "AABCAAADA"
n = len(s)
k = 3
plen = len(s) // k

li = []

for i in range(0,n,plen):
    partition = s[i:i+plen]
    li.append(partition)


# print(li)

def finddistnc(c):
    diststr = ""
    for i in range(len(c)):
        if c[i] not in diststr:
            diststr += c[i]
    return diststr


for i in range(len(li)):
    str = li[i]
    # print(str)
    print(finddistnc(str))



# print distinct char


