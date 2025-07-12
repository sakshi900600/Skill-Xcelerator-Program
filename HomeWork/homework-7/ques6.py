# 6. Basic Calculator (with parentheses) 
# Description: Implement a basic calculator to evaluate a string expression with +, -, and (). 
# Input: 
s = "(1+(4+5+2)-3)+(6+8)" 

# Output: 
# 23


def infix(s):
    li = []
    st = []
    for i in range(len(s)):
        if s[i].isdigit():
            st.append(int(s[i]))
        
        elif s[i] == ')':
            ind = len(li)-1
            while st and li and li[ind] != '(':
                op = li.pop()
                e2 = st.pop()
                e1 = st.pop()
                res = f"{e1}{op}{e2}"
                st.append(res)
                ind -= 1

        else:
            li.append(s[i])
    

    return st.pop()



op_stack = []
num_stack = []

for i in range(len(s)):
    if s[i].isdigit():
        num_stack.append(int(s[i]))
    elif s[i] == ")":
        dljf
        

# print(infix(s))



