#  Create Team Groups with Player Count

players = { 
  "Messi": "PSG", 
  "Ronaldo": "Al-Nassr", 
  "Mbappe": "PSG", 
  "Neymar": "PSG" 
}

# output: {'PSG': 3, 'Al-Nassr': 1}

final_dct = {}

for player, team in players.items():
    if team not in final_dct:
        final_dct[team] = []
    final_dct[team].append(player)

# print(final_dct)


for team,name in final_dct.items():
    final_dct[team] = len(name)


print(final_dct)
