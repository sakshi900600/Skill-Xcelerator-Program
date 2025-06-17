# Find Longest Word with All Vowels

words = ["sequoia", "education", "automobile", "abstemious"]

words = sorted(words)

# how to check all vowels present in a string
def isvowel_present(str):
    vowels = {'a','e','i','o','u'}
    str = str.lower()
    return vowels.issubset(str)


# print(isvowel_present("sequoia"))


# output:  abstemious
maxlen = 0
word = ""
for i in range(len(words)):
    if isvowel_present(words[i]):
        length = len(words[i])
        if length > maxlen:
            maxlen = length
            word = words[i]


# print(maxlen)
print(word)


