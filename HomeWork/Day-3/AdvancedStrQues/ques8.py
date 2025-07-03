# Find the smallest substring that contains all characters of a given target string.  
# Input: s = "ADOBECODEBANC", t = "ABC" → Output: "BANC"


s = "ADOBECODEBANC"
t = "ABC"

# print(s.find(t))

minlen = float('inf')

for i in range(len(s)):
    for j in range(i, len(s)):
        subStr = s[i:j+1]
        # subStr = sorted(subStr)
        if t in subStr:
            length = j-i+1
            minlen = min(minlen,length)


print(minlen)