# replace digits with # in string
#  Input: "Room 101 is on floor 2" → Output: "Room ### is on floor #"


# s = "Room 101 is on floor 2"
s = "Hello 1234 welcome 2 345"  #output: Hello #### welcome # ###
newStr = ""
for i in range(len(s)):
    if s[i].isdigit():
        newStr += '#'
    else:
        newStr += s[i]

print(newStr)