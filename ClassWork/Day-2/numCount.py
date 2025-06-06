s = "13343442425"

i = 0
for j in range(len(s)):
    count=0
    if s[j]==s[i]:
        count += 1

    if count != s[i]:
        print(s[i])
