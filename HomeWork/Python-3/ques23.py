# Count frequency of each word.


# {'gravity': 1, 'is': 2, 'force': 2, 'and': 1, 'mass': 1, 'times': 1, 'acceleration': 1}
s = "gravity is force and force is mass times and is times acceleration"


s = s.split()
dct = {}


for i in range(len(s)):
    dct[s[i]] = dct.get(s[i],0)+1

print(dct)