# Filter Words Starting and Ending with Same Letter 

words = ["radar", "rotor", "hello", "world", "mom"] 
 
# Output: ['radar', 'rotor', 'mom']

for i in range(len(words)):
    str = words[i]

    if str[0] == str[len(str)-1]:
        print(str)