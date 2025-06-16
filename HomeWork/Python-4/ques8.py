# Task: Reverse the dictionary to group players by team. 


players = { 
  "Messi": "PSG", 
  "Ronaldo": "Al-Nassr", 
  "Mbappe": "PSG" 
} 
 
# Expected Output: 
{ 
  "PSG": ["Messi", "Mbappe"], 
  "Al-Nassr": ["Ronaldo"] 
}



final_dct = {}


for player, team in players.items():
    if team not in final_dct:
        final_dct[team] = []
    final_dct[team].append(player)
    

print(final_dct)
    
    