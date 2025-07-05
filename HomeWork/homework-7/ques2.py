# s = "1432219"
# k = 3

s = "10"
k = 2

# s = "10200"
# k = 1

stack = list()

for i in range(len(s)):
    while stack and int(stack[-1]) > int(s[i]) and k > 0:
        stack.pop()
        k -= 1
    
    stack.append(s[i])


ans = stack
if k > 0:
    ans = stack[0:len(stack)-k]

final_str = "".join(ans)

if final_str == "":
    final_str = '0'


print(final_str.lstrip('0'))

# print(n.ljust('0'))