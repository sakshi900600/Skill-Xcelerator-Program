# count freq of each vowel, Return a dictionary with counts of each vowel in the string.

# Input: "education" → Output: {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}


# way 1 -------------------------------------------------------
s = "education" # output: {'e': 1, 'u': 1, 'a': 1, 'i': 1, 'o': 1}

dict = dict()
for char in s.lower():
    if char in {'a', 'e', 'i','o','u'}:
        dict[char] = dict.get(char,0)+1
    

print(dict)


# way -2 to print a,e,i,o,u  -------------------------------------

t = "Sakshi"
vowels = {'a':0, 'e':0, 'i':0,'o':0, 'u':0}

for char in t.lower():
    if char in vowels:
        vowels[char] += 1

print(vowels)
