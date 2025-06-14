s = "ABCDE"

dct = {"a","e", "i","o","u"}
vowels = 0
const = 0
s  = s.lower()

for i in range(len(s)):
    if s[i] in dct:
        vowels += 1
    else:
        const += 1

print(vowels)
print(const)


# for i in range(len(s)):
    