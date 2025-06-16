# Create Index-Based Patient Lookup 

patients = ["Alice", "Bob", "Cara"] 
 
# Output: {0: "Alice", 1: "Bob", 2: "Cara"}

dct = {}

for i in range(len(patients)):
    dct[i] = patients[i]

print(dct)

