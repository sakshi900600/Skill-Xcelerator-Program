# Filter Critical Patients from Records 
# Condition: BP > 130 and Sugar > 180 is critical. 

# Expected Output: ['Alice', 'Cara']

patients = [ 
  {"name": "Alice", "bp": 140, "sugar": 200}, 
  {"name": "Bob", "bp": 120, "sugar": 150}, 
  {"name": "Cara", "bp": 160, "sugar": 220} 
] 
 

# print(patients[0]['name'])
# print(patients[0]['scores'])

li = []

for i in range(len(patients)):
    name = patients[i]['name']
    bp = patients[i]['bp']
    sugar = patients[i]['sugar']
    
    if bp > 130 and sugar > 180:
        li.append(name)

print(li)
