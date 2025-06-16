# Remove Duplicates from String List and Sort

words = ["atom", "molecule", "atom", "compound", "molecule"]

# output: ['atom', 'compound', 'molecule']

words = sorted(words)

li = []
for i in range(len(words)):
    if words[i] not in li:
        li.append(words[i])

print(li)

