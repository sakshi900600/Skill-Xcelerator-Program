# Minimize String by Removing K Characters to Get Lexicographically Smallest 
#  Remove k characters to get the smallest possible string in dictionary order.  

#  Input: "cbacdcbc", k=2 → Output: "acdbc"

# I think output is wrong, coz here 3 char is removed.

s = "cbacdcbc"
k = 2
print(ord(s[0]))
print(ord(s[1]))

for i in range(len(s)-1):
    while k >=0:
        if ord(s[i]) > ord(s[i+1]):
            s = s.replace(s[i],"")
            k -= 1


print(s)
