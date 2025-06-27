# create a matrix in which 4 elem and inside that elem list should be multiiple


li = []

for i in range(2,6):
    x = 1
    temp = []
    while x<= 10:
        temp.append(i*x)
        x += 1

    li.append(temp)

print(li)


