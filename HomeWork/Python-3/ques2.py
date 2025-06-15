# Input: match_scores = {'TeamA': 3, 'TeamB': 2} 
#  Task: Print which team won or print "Draw".  Expected Output: "TeamA wins"


match_scores = {'TeamA': 3, 'TeamB': 2}

if match_scores['TeamA'] > match_scores['TeamB']:
    print('TeamA wins')
elif match_scores['TeamA'] == match_scores['TeamB']:
    print("match draw")