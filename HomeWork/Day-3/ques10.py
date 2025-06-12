# Generate All Valid Parentheses Strings of Length 2n

#  Input: n = 3 → Output: ["((()))", "(()())", "(())()", "()(())", 
# "()()()"]


def generate_parenthesis(li, open, close, n, str):
    if(len(str) == 2*n):
        li.append(str)
        return
    if(open < n):
        generate_parenthesis(li, open+1, close, n, str+'(')
    if(close < open):
        generate_parenthesis(li, open, close+1, n, str+')')


def parenthesis(n):
    li = []
    generate_parenthesis(li,0,0,n, "")
    return li


n = 2 # output: ['(())', '()()']
n = 3 # output: ['((()))', '(()())', '(())()', '()(())', '()()()']
result = parenthesis(n)
print(result)
        