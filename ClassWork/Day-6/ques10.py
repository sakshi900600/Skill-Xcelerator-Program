#  Skip "Candy" while listing food items using continue

foods = ["Apple", "Candy", "Banana"]

for item in foods:
    if item == "Candy":
        continue
    else:
        print(item)


# output:
# Apple
# Banana