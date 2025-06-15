# 4. 🏥 Patient Fever Detection 
#  Task: Print names of patients who have a temperature above 100. 

# Input: patients = {'John': 98.6, 'Priya': 101.4, 'Ali': 99.0, 'Neha': 103.5} 
# 
#  Expected Output: ['Priya', 'Neha']


patients = {'John': 98.6, 'Priya': 101.4, 'Ali': 99.0, 'Neha': 103.5}
li = list()

for name,temp in patients.items():
    if temp > 100:
        li.append(name)


print(li)