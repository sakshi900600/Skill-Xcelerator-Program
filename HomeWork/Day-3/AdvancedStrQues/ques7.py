# Take a sentence and return it in multiple coding styles. 
#  Input: "convert this sentence" → 
# Output: 
# ●  camelCase: "convertThisSentence"  
# ●  PascalCase: "ConvertThisSentence"
# ●  kebab-case: "convert-this-sentence"


# s = "convert this sentence"
s = "hello welcome sakshi"
s = s.split(" ")

camelCase = ""
PascalCase = ""
kebab_case = "-".join(s)


# print(s)

for word in s:
    PascalCase += "".join(word.capitalize())


camelCase += s[0]
for word in s[1:]:
    camelCase +=  "".join(word.capitalize())


print(camelCase)
print(PascalCase)
print(kebab_case)
