# 1. 🏏 Cricketer's Jersey Filter 
# Input: players = [('Kohli', 18), ('Dhoni', 7), ('Rohit', 45), ('Pant', 17)] 
#  Task: Print the names of players whose jersey numbers are multiples of 3.  

# Expected Output: ['Kohli']

players = [('Kohli', 18), ('Dhoni', 7), ('Rohit', 45), ('Pant', 17)]
dct = dict(players)


for player,jersey in dct.items():
    if jersey % 3 == 0:
        print(player)

