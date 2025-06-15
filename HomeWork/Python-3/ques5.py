# Player Name Validator 
#  Task: Print all names with length greater than 5.  

# Input: player_names = ['Messi', 'Neymar', 'Mbappe', 'Suarez'] 
# Expected Output: ['Neymar', 'Mbappe', 'Suarez']


player_names = ['Messi', 'Neymar', 'Mbappe', 'Suarez']

for player in player_names:
    if len(player) > 5:
        print(player)