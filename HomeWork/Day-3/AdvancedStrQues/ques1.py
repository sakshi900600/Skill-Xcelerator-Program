# decode nested encoded string: 
#  Implement a decoder that can handle nested encoding rules of the form k[encoded_string], 
# where k is a number and encoded_string is repeated k times.  

# Input: "3[a2[c]]" → Output: "accaccacc"

# s = "ab"
# print(3*s)


s = "3[a2[c]]"

s = s.replace('[', '*')
# print(s)

ans = ""
for i in range(len(s)-1, 0):
    if(s[i] == '*'):
        s1 = s[i-1]
        s2 = s[i+1]
        s = s.replace()
        ans += res
    

print(ans)
