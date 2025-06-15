# Calculate and print total goals for each day


# output: {'Mon': 3, 'Tue': 3, 'Wed': 4}

matches = [ 
    {'day': 'Mon', 'goals': [1, 2]}, 
    {'day': 'Tue', 'goals': [0, 3]}, 
    {'day': 'Wed', 'goals': [2, 2]} 
]

# print(matches[0]['goals'])
# print(sum(matches[0]['goals']))

dct = {}

for i in range(len(matches)):
    day = matches[i]['day']
    glist = matches[i]['goals']
    total = sum(glist)

    dct[day] = total


print(dct)

