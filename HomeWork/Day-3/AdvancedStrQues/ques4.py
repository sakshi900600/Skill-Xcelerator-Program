# # Given a string of sorted alphanumeric characters, find missing ranges.  
# #  Input: "12346789BCDF" → Output: ["5", "A", "E"]


# # want clarification: 
# # 1. if digit in input will start from 2/3 then whether 1,2 will be consider as missing or not. 


# I have assumed that: 
# 1.  for char it will be always between A to last char in given string and i have to find out all missing char between them and if there is no missing char then add the char after last char

# 2.  for number it will be always from 1 to 9 but missing will be only b/n 1 to last digit in num. if not then digit after last digit and if last digit is 9 then nothing is missing. 



# s = "12346789ABCDEF"  # output: ['5', 'G']
s = "2346789BCDF"  # output: ['5', 'G']

num = ""
character = ""


for i in range(len(s)):
    if s[i].isdigit():
        num += s[i]
    elif s[i].isalpha():
        character += s[i]

# print(num)
# print(str)

li = list()


# checking missing no
lastdigit = int(num[-1])

for i in range(1, lastdigit):
    if str(i) not in num:
        li.append(str(i))





start = ord('A')
end = ord(character[-1])

# add all missinsg char in list
temp = []
while start < end:
    if chr(start) not in character:
        temp.append(chr(start))
        li.extend(temp)
    start += 1

# if not any char missing then add char after last char.
if not temp:
    char = chr(end+1)
    li.append(char)


print(li)
# print(ord('E'))



