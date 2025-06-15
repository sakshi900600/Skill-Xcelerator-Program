# Print "High" for age ≥ 60, "Medium" for 40–59, "Low" otherwise


# Output: ['Low', 'High', 'Medium', 'High', 'Low']
patients = [25, 60, 45, 72, 15]

for i in range(len(patients)):
    age = patients[i]
    if age >= 60:
        print("High")
    elif age>=40 and age<=59:
        print("Medium")
    else:
        print("Low")
