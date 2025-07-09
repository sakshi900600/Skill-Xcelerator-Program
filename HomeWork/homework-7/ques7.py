#  7. Longest Valid Parentheses 
# Description: Given a string of ( and ), find the length of the longest valid (well-formed) parentheses 
# substring. 
# Input: 
# s = "(()))())(" # 4
# s = "()(()"  # 2

s = ")()())"  # 4

# Output: 
# 4

n = len(s)
st = []
maxlen = 0

for i in range(n):
    temp_len = 0
    if s[i] == '(':
        st.append(i)
    
    elif s[i] == ')':
        if len(st) == 0:
            temp_len = 0
        else:
            # open_idx = st.pop()
            temp_len = i - st[-1] + 1
        
        maxlen = max(maxlen, temp_len)


print(maxlen)