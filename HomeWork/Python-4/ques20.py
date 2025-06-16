# Count Letter Frequency in All Patient Names

# doubt: here A and a is same but B and b is not same why???????????????


names = ["Alice", "Bob", "Cara"]

# output: {'A': 2, 'l': 1, 'i': 1, 'c': 2, 'e': 1, 'B': 1, 'o': 1, 'r': 1}

dct = {}

for i in range(len(names)):
    str = names[i]
    for j in range(len(str)):
        dct[str[j]] = dct.get(str[j],0)+1


print(dct)