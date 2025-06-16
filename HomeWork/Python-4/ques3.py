# Count and return the most frequent letter (a–z only)

data = "covid19spread2023"
# output: Most Frequent Character: d


dct = {}

for i in range(len(data)):
    if data[i].isalpha():
        dct[data[i]] = dct.get(data[i],0)+1

# print(dct)
maxFreq = 0
mostFreqChar = ''
for key, value in dct.items():
    if value > maxFreq:
        maxFreq = value
        mostFreqChar = key


print(mostFreqChar)