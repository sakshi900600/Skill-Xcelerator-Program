# Count Letter Frequency in All Patient Names

# doubt: here A and a is same but B and b is not same why???????????????


names = ["Alice", "Bob", "Cara"]

#expected output: {'A': 2, 'l': 1, 'i': 1, 'c': 2, 'e': 1, 'B': 1, 'o': 1, 'r': 1}
# output: {'A': 1, 'l': 1, 'i': 1, 'c': 1, 'e': 1, 'B': 1, 'o': 1, 'b': 1, 'C': 1, 'a': 2, 'r': 1}

dct = {}

for i in range(len(names)):
    str = names[i]
    for ch in str:
        dct[ch] = dct.get(ch,0)+1


print(dct)