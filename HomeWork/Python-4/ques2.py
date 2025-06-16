# Print the team with the longest name and the number of vowels in it.

teams = ["Barcelona", "Juventus", "ParisSaintGermain", "Chelsea"]

# output: Team: ParisSaintGermain, Vowels: 7

name = ""
maxlen = 0
for i in range(len(teams)):
    if len(teams[i]) > maxlen:
        maxlen = len(teams[i])
        name = teams[i]
    


# print(name)

dct = {'a','e','i','o','u'}
count = 0

for i in range(len(name)):
    if name[i] in dct:
        count += 1

print(f"Teams: {name}, vowels: {count}")