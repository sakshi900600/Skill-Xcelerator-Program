# Move all zeros at the end: [1,3,12,0,0]

# li = [0,1,0,3,12]

li = [0,1,0,4,6,8]

newList = list()

for i in range(len(li)):
    if li[i] != 0:
        newList.append(li[i])


newList.extend([0] * (len(li) - len(newList)))

print(newList) 
