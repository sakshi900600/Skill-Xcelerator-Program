#  Print total goals scored in even-numbered matches (0-based indexing).


# Output: 0 + 2 + 3 = 5
goals = [0, 1, 2, 0, 3, 2] #(each index = match number)

total_goals = 0
for i in range(len(goals)):
    if i%2 == 0:
        total_goals += goals[i]

print(total_goals)