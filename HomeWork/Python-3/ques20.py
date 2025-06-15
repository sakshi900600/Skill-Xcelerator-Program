# Assign rooms in format: Room-1: Amit, Room-2: Neha...

# Output: ['Room-1: Amit', 'Room-2: Neha', 'Room-3: John', 'Room-4: 
# Sara']


patients = ['Amit', 'Neha', 'John', 'Sara']

li = []

for i in range(len(patients)):
    str = f'Room-{i+1}' 
    li.append(str + ": " + patients[i])


print(li)