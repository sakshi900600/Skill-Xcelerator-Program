#  Create a new dictionary where keys are player names and values are their average scores. 


players = [ 
  {"name": "Kohli", "scores": [54, 76, 102, 90]}, 
  {"name": "Rohit", "scores": [45, 88, 60, 40]}, 
  {"name": "Gill", "scores": [70, 80, 77, 120]} 
]


# output:  {'Kohli': 80.5, 'Rohit': 58.25, 'Gill': 86.75}

dct = {}

# print(players[0]['name'])
# print(players[0]['scores'])


def average(li):
    sum = 0
    for i in range(len(li)):
        sum += li[i]
    
    avg = sum/len(li)
    return avg


for i in range(len(players)):
    name = players[i]['name']
    scores = players[i]['scores']
    avg = average(scores)
    dct[name] = avg


print(dct)


