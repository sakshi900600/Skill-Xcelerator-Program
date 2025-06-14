# Given a string of sorted alphanumeric characters, find missing ranges.  
#  Input: "12346789BCDF" → Output: ["5", "A", "E"]


# want clarification: 
# 1. will string always start with digit and if digit in input will start from 2 then whether 1 will be consider as missing or not. 


s = "12346789BCDF"

for i in range(1, len(s)):
    if s[i].isdigit():
        if s[i] != int(s[i-1])+1:
            print(int(s[i])-1)

