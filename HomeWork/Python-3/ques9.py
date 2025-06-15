# 9. Goal Difference Detector 
#  Task: If it's a draw, print "Extra Time". Else print goal difference. 


# Input: match = {'TeamA': 2, 'TeamB': 2} 
#  Expected Output: "Extra Time"

match = {'TeamA': 8, 'TeamB': 9}

if match['TeamA'] == match['TeamB']:
    print("Extra Time")
else:
    print(abs(match['TeamA'] - match['TeamB']))