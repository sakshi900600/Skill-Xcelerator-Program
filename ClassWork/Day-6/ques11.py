# Simulate rolling dice. Stop when 6 appears

Input = [2, 5, 4, 6, 3]

for item in Input:
    if item == 6:
        break
    else:
        print(f"Rolled {item}")


# output: 
# Rolled 2
# Rolled 5
# Rolled 4