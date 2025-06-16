# Merge Two Player Stat Dictionaries

a = {"Kohli": 70, "Gill": 80} 
b = {"Rohit": 60, "Gill": 85}

# output: {'Kohli': 70, 'Gill': 85, 'Rohit': 60}

dct = {}

for name,score in a.items():
    dct[name] = score

for name,score in b.items():
    dct[name] = score

print(dct)