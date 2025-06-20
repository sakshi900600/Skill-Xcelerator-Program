# Loop through signals. Break when "Red" is found. 

Input = ["Green", "Yellow", "Red", "Green"]

for item in Input:
    if item == "Red":
        print(f"{item} Light! Stop!")
        break
    else:
        print(item)

#output:
# Green
# Yellow
# Red Light! Stop!