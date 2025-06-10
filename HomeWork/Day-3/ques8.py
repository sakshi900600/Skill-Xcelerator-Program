# find all words that appers exactly once
#  Input: "apple orange banana apple mango" → Output: ["orange", "banana", 
# "mango"]

# s = "apple orange banana apple mango"
s = "sakshi riya ritu sakshi sam"  #output: ['riya', 'ritu', 'sam']
s = s.split(" ")
dict = dict()
for char in s:
    dict[char] = dict.get(char,0)+1

# print(dict)

list = list()
for key,value in dict.items():
    if value == 1:
        list.append(key)

print(list)