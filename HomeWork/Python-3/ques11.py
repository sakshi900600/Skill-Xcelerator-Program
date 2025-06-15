#  Task: Reverse each word but maintain order.  

# Input: "experiment successful theory failed" 

# Expected Output: "tnemirepxe lufsseccus yroeht deliaf"

# s = "experiment successful theory failed" 

s = "Hey there! Welcome to kota"

s = s.split(" ")
# print(s)

ans = ""

for i in range(len(s)):
    word = s[i]
    revWord = word[:: -1]
    ans += revWord
    ans += " "

print(ans)

