# # Given a string of sorted alphanumeric characters, find missing ranges.  
# #  Input: "12346789BCDF" → Output: ["5", "A", "E"]


# # want clarification: 
# # 1. if digit in input will start from 2/3 then whether 1,2 will be consider as missing or not. 


# I have assumed that: 
# 1.  for char it will be always between A to last char in given string and i have to find out all missing char between them and if there is no missing char then add the char after last char

# 2.  for number it will be always from 1 to 9 but missing will be only b/n 1 to last digit in num. if not then digit after last digit and if last digit is 9 then nothing is missing. 



# s = "12346789ABCDEF"  # output: ['5', 'G']
# s = "12346789BCDF"  # output: ['5', 'A', 'E']
# s = "2356ACDE" # output: ['1', '4', 'B']
s = "2345789ABCD"  # output: ['1', '6', 'E']

num = ""
character = ""


for i in range(len(s)):
    if s[i].isdigit():
        num += s[i]
    elif s[i].isalpha():
        character += s[i]

# print(num)
# print(str)

def missingNumber(num):
    
    li1 = list()

    # checking missing no
    lastdigit = int(num[-1])

    for i in range(1, lastdigit):
        if str(i) not in num:
            li1.append(str(i))


    # if nothing is missing:
    if not li1:
        if lastdigit != 9:
            li1.append(lastdigit+1)

    return li1



def missingChar(character):
    start = ord('A')
    end = ord(character[-1])

    # add all missinsg char in list
    li2 = []
    for i in range(start,end):
        if chr(i) not in character:
            li2.append(chr(i))

    # if not any char missing then add char after last char.
    if not li2:
        char = chr(end+1)
        li2.append(char)

    return li2


li1 = missingNumber(num)
li2 = missingChar(character)

ans = []
ans.extend(li1)
ans.extend(li2)
print(ans)



