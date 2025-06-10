# longest palindromic substring:
#  Input: "babad" → Output: "bab" or "aba"


# s = "babad"  #output: bab
# s = "racecar"  # output: racecar
s = "abcde" #output: a

max = 0
longPsubStr = ""
for i in range(len(s)):
    for j in range(i, len(s)):
        subStr = s[i: j+1]
        if subStr == subStr[::-1]:
            if len(subStr) > max:
                max = len(subStr)
                longPsubStr = subStr
            

print(longPsubStr)