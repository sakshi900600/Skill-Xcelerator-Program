# Find Most Common Disease


diagnoses = ["Diabetes","Covid", "Covid", "Flu", "Covid", "Flu"]
# output:  Most common disease: Flu

dct = {}

for i in range(len(diagnoses)):
    dis = diagnoses[i]
    dct[dis] = dct.get(dis,0)+1

# print(dct)
maxcount = 0
maxcountdis = ""
for name,count in dct.items():
    if count > maxcount:
        maxcount = count
        maxcountdis = name

print(maxcountdis)
    