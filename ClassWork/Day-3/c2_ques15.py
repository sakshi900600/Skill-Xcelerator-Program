s = "Backend Developers"

print(s.split(" "))

newStr = s.split()
acronym = "".join(word[0] for word in newStr)
print(acronym)