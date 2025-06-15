# Print players who scored 100 or more


# Output: ['Kohli', 'Rohit']
players = {'Rahul': 75, 'Kohli': 102, 'Rohit': 120}

for name,score in players.items():
    if score >= 100:
        print(name)