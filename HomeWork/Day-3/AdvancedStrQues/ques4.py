# Given a string of sorted alphanumeric characters, find missing ranges.  
#  Input: "12346789BCDF" → Output: ["5", "A", "E"]


# want clarification: 
# 1. will string always start with digit and if digit in input will start from 2/3 then whether 1,2 will be consider as missing or not. 


s = "12346789BCDF"
num = ""
str = ""


for i in range(len(s)):
    if s[i].isdigit():
        num += s[i]
    elif s[i].isalpha():
        str += s[i]



print(num)
print(str)

li = list()


# checking missing no
for i in range(len(num)-1):
    if int(num[i+1]) - int(num[i]) != 1:
        li.append(int(num[i]) +1)


# checking missing alphabet
for i in range(len(str)-1):
    if(ord(str[i+1]) - ord(str[i]) != 1):
        ch = chr(ord(str[i])+1)
        li.append(ch)




print(li)
print(ord('E'))
