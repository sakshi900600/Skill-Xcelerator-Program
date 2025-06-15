# Calculate BMI = weight / (height ** 2) and print name if BMI > 24

# Output: ['Ankit']
patients = [ 
    {'name': 'Ankit', 'height': 1.7, 'weight': 70}, 
    {'name': 'Neha', 'height': 1.6, 'weight': 55} 
]


for i in range(len(patients)):
    h = patients[i]['height']
    w = patients[i]['weight']
    bmi = w / (h ** 2)
    if bmi > 24:
        name = patients[i]['name']
        print(name)