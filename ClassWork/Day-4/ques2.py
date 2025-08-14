# you are give 2 lists and you have to create new list in which add the common elem of both lists and sort and print the list


l1 = [1,2,3,4]
l2 = [3,2,9,8,4]

lans = list()

for i in range(len(l1)):
    if l1[i] in l2:
        lans.append(l1[i])

lans.sort(reverse=True)
# print(lans)



lans = sorted(set(l1) & set(l2), reverse=True)
print(lans)