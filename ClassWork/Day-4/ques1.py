# give a list you have to print elem whose freq is second 

li = [1,2,2,3,3,1,1,1,2]

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

print(highestFreq2)
print(highestFreq2elem)


# logic: 2 
# store freq of all list elem using li.count (by applying loop)
# then sort the freq list and get second freq elem.
# 
#  

