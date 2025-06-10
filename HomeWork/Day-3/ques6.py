# find most frequent word in sentence:
# Input: "The fox jumped over the lazy dog. The dog barked." → 
#  Output: "the

# s = "The fox jumped over the lazy dog. The dog barked." #output: the
s = "The fox fox fox fox jumped over the lazy dog. The dog barked." #output: fox

s = s.lower()
s = s.split(" ")
# print(s)

dict = dict()

for char in s:
    dict[char] = dict.get(char,0)+1

print(dict)
# print(max(dict)) - gives wrong output

maxfreq = 0
mostFrequent = ""
for key, value in dict.items():
    if value > maxfreq:
        maxfreq = value
        mostFrequent = key

# print(maxfreq)
print(mostFrequent)


