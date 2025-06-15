# 8. 🏥 Filter Stable Patients 

# Input: 
# patients = [ 
#     {'name': 'Amit', 'bp': 120}, 
#     {'name': 'Sara', 'bp': 140}, 
#     {'name': 'Mike', 'bp': 130} 
# ] 
# Expected Output: ['Amit']
 
# Task: Print patients with bp < 130.  


patients = [ 
    {'name': 'Amit', 'bp': 120}, 
    {'name': 'Sara', 'bp': 100}, 
    {'name': 'Mike', 'bp': 130} 
] 

# print(patients[0].get('name'))
# print(patients[0].get('bp'))


for i in range(len(patients)):
    bp = patients[i].get('bp')
    if bp < 130:
        name = patients[i].get('name')
        print(name)