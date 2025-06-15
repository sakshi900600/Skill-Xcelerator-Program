# 13. ⚽ Goals from Top 3 Players 
# Input: 
# goals = { 
#     'Ronaldo': 9, 
#     'Messi': 13, 
#     'Neymar': 7, 
#     'Mbappe': 11 
# } 
 
# Task: Print top 3 players by goals scored.  

# Output: ['Messi', 'Mbappe', 'Ronaldo']


goals = { 
    'Ronaldo': 9, 
    'Messi': 13, 
    'Neymar': 7, 
    'Mbappe': 11 
} 

max1 = 0
max2 = 0
max3 = 0

max1P = ""
max2P = ""
max3P = ""

for player,goal in goals.items():
    if goal> max1:
        max3 = max2
        max2 = max1
        max1 = goal
        max1p = player
    elif goal > max2:
        max3 = max2
        max2 = goal
        max2p = player
    elif goal > max3:
        max3 = goal
        max3p = player


print(max1, max2, max3)
print(max1p, max2p, max3p)