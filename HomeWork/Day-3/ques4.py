# compress the string

# Input: "aaabbcddd" → Output: "a3b2cd3"

# s = "aaabbcddd"  # output: a3b2cd3
s = "ddeefggghi" #output: d2e2fg3hi

dict =  dict()
for char in s:
    dict[char] = dict.get(char,0)+1

# print(dict)
# print(dict.keys())
# print(dict.values())
# print(dict.items())

newStr = ""
for key, value in dict.items():
    if(value > 1):
        temp = key + str(value)
        newStr += temp
    else:
        temp = key
        newStr += temp

print(newStr)


