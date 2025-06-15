# Input: players = ['Virat Kohli', 'MS Dhoni', 'Rohit Sharma'] 
#  Task: Print initials of last names.  

# Expected Output: ['K', 'D', 'S'] 

players = ['Virat Kohli', 'MS Dhoni', 'Rohit Sharma']


li = []
for item in players:
    li.append(item.split(" "))

for i in range(len(li)):
    last_name = li[i][1]
    # print(li[i][1])
    print(last_name[0])