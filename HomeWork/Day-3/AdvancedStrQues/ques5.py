# Find Longest Valid Mathematical Expression 
#  From a string, extract and return the longest valid mathematical expression.  

# Input: "abc1+2*3xyz4-5/2ab" → Output: "1+2*3"


s = "abc1+2*3xyz4-5/2*3ab"

maxlen = 0
maxlenexp = ""

currexp = ""

for i in range(len(s)):
    if not s[i].isalpha():
        currexp += s[i]
    else:
        if(len(currexp) > maxlen):
            maxlen = len(currexp)
            maxlenexp = currexp
            currexp = ""


print(maxlenexp)
print(maxlen)