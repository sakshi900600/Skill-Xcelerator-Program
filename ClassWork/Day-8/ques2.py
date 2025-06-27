
f = [0] * 100


f[0], f[1] = 0,1
for i in range(2,100):
    num = f[i-1] + f[i-2]
    f.insert(i, num)


# print(f)

inp = [23,1,3,4,8]

ans = []

for i in inp:
    ans.append(f[i-1])

print(ans)