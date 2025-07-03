# Minimize String by Removing K Characters to Get Lexicographically Smallest 
#  Remove k characters to get the smallest possible string in dictionary order.  

#  Input: "cbacdcbc", k=2 → Output: "acdbc"
# I think output is wrong, coz here 3 char is removed.


s = "cbacdcbc"
# k = 2  # output: acdcbc
k = 4 # output: acbc

# print(ord(s[0]))
# print(ord(s[1]))

# we will use stack using list: 
#  push: li.append(elem)
#  pop: li.pop()
#  peek: li[-1]
#  is_empty: len(li) == 0


stack = list()

for i in range(len(s)):
    while stack and ord(stack[-1]) > ord(s[i]) and k > 0:
        stack.pop()
        k -= 1
    
    stack.append(s[i])


ans = stack
if k > 0:
    ans = stack[0:len(stack)-k]

final_str = "".join(ans)
print(final_str)
