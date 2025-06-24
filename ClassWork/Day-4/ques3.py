# count and print freq of elem in list

li = [1,2,3,"abc","abc", "abc" ,True]



freq = {}

for i in li:
    freq[i] = freq.get(i,0)+1


print(freq)