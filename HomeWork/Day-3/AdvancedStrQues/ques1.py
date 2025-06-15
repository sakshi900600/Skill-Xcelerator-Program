# decode nested encoded string: 
#  Implement a decoder that can handle nested encoding rules of the form k[encoded_string], 
# where k is a number and encoded_string is repeated k times.  

# Input: "3[a2[c]]" → Output: "accaccacc"

# s = "ab"
# print(3*s)


s = "3[a2[c]]"

# s = s.replace('[', '')
# print(s)

s = s[:: -1]
print(s)
# print(s*2)

ans = ""
curr_str = ""

for i in range(len(s)):
    if s[i].isalpha():
        curr_str += s[i]
    
    if s[i].isdigit():
        ans += curr_str * int(s[i])
        curr_str = ""
        
    

print(ans)
