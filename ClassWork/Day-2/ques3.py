# find toop 3 max value in list without sorting the list

a = [2,5,8,1,9]

max1 = a[0]
max2 = a[0]
max3 = a[0]

for i in range(len(a)):
    if(a[i] > max1):
        max3 = max2
        max2 = max1
        max1 = a[i]
    elif(a[i] > max2):
        max3 = max2
        max2 = a[i]
    elif(a[i] > max3):
        max3 = a[i]


print(max1)
print(max2)
print(max3)
