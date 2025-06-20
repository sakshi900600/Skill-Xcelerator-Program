# Print each item in a backpack with its position using enumerate

backpack = ["Water", "Map", "Snacks"]

for idx,item in enumerate(backpack):
    print(f"{idx+1}. {item}")