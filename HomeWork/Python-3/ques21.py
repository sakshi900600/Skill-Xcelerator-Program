# Sort and print names in increasing order of their length

# Output: ['Pele', 'Messi', 'Maradona', 'Cristiano']
li = ['Messi', 'Cristiano', 'Pele', 'Maradona']

sortedLi = sorted(li, key=len)

for names in sortedLi:
    print(names)



