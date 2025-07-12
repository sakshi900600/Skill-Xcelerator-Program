#  5. Decode String 
# Description: Decode an encoded string with nested patterns like 3[a2[c]] → accaccacc. 
# Input: 
s = "3[a2[c]]" # accaccacc
 

# s = "3[a]2[bc]"  # aaabcbc

# s = "2[abc]3[cd]ef"  # abcabccdcdcdef


n = len(s)
st = []
ans = ""
cnum = 0
cstr = ""


for i in range(n):
    if s[i].isdigit():
        cnum = cnum * 10 + int(s[i])
    
    if s[i].isalpha():
        cstr += s[i]
    
    if s[i] == '[':
        st.append([cnum,cstr])
        cnum = 0
        cstr = ""
    
    if s[i] == ']':
        pnum = st[-1][0]
        pstr = st[-1][1]
        st.pop()
        cstr = pstr + (pnum * cstr)


print(cstr)



