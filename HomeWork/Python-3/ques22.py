# Identify and print duplicate names

# Output: ['Kohli']
li = ['Kohli', 'Dhoni', 'Rohit', 'Kohli', 'Pant', "Dhoni"]

dct = {}

for i in range(len(li)):
    dct[li[i]] = dct.get(li[i],0)+1

# print(dct)

for name,count in dct.items():
    if count > 1:
        print(name)
