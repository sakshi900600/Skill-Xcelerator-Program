# Find the smallest substring that contains all characters of a given target string.  
# Input: s = "ADOBECODEBANC", t = "ABC" → Output: "BANC"


s = "ADOBECODEBANC"
t = "ABC"

print(s.find(t))

smallest = len(s)
small_subStr = ""

for i in range(len(s)):
    for j in range(i, len(s)):
        subStr = s[i:j+1]
        if t in subStr:
            if smallest > len(subStr):
                smallest = len(subStr)
                small_subStr += subStr
            # print("yes")
            break


print(smallest)
print(small_subStr)