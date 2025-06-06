# s = "ABCdJ2398Dd92C8d"
# find sum of all numbers in string
# output = 2398 + 92 + 8 = 2498

s = input("enter a string: ")
n = len(s)
num = 0
ans = 0

for i in range(n):
    if s[i].isdigit():
        num = (num * 10) + int(s[i])
    else:
        ans += num
        num = 0

ans += num
print(ans)