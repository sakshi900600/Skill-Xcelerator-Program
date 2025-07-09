#  5. Decode String 
# Description: Decode an encoded string with nested patterns like 3[a2[c]] → accaccacc. 
# Input: 
s = "3[a2[c]]" 
 
# Output: 
# "accaccacc"


# s = s.replace('[', "")

st = []
n = len(s)
ans = ""
for i in range(n):
    if s[i] != ']':
        st.append(s[i])
    
    else:
        while not st[-1].isdigit():
            elem = st.pop()
            if elem.isalpha():
                ans = ans + elem
            
            elif elem.isdigit():
                ans = int(elem) * ans


print(st)
print(ans)





2 * "ldkjf"
print(ans)



