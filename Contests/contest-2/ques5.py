s = "1234"

s = s.replace("", " ")
s = s.split()
# print(s)

for i in range(1, len(s)):
    if s[i] - s[i-1] != 1:
        print("NO")
    


