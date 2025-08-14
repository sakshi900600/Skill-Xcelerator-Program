# given a list you have to print elem whose freq is second largest

li = [1,2,2,3,3,1,1,1,2]
# li = [1,1,2,3,5]

highestFreq1 = 0
highestFreq2 = 0
highestFreq1elem = li[0]
highestFreq2elem = li[0]

for i in range(len(li)):
    freq = li.count(i)
    if(freq > highestFreq1):
        highestFreq1 = freq
        highestFreq1elem = li[i]
    elif(freq > highestFreq2 and freq != highestFreq1):
        highestFreq2 = freq
        highestFreq2elem = li[i]

# print(highestFreq2)
print(highestFreq2elem)



# logic: 2 
dct = {}

for i in li:
    dct[i] = dct.get(i,0)+1

des_sorted_val = sorted(dct.values(), reverse=True)

sec_larg_freq = des_sorted_val[1]

for k,v in dct.items():
    if v == sec_larg_freq:
        print(k)
