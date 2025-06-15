# Task: Print names of patients with odd ages. 

# Input: 
# patients = [ 
#     {'name': 'John', 'age': 28}, 
#     {'name': 'Anita', 'age': 35}, 
#     {'name': 'Karan', 'age': 30} 
# ] 
 
#  Expected Output: ['Anita'] 


patients = [ 
    {'name': 'John', 'age': 28}, 
    {'name': 'Anita', 'age': 35}, 
    {'name': 'Karan', 'age': 30} 
] 

# print(patients[0]['name'])

for i in range(len(patients)):
    age = patients[i]['age']

    if age % 2 != 0:
        name = patients[i]['name']
        print(name)