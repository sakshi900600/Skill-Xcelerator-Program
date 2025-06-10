# check for substring rotation

#  Input: "waterbottle", "erbottlewat" → Output: True

s = "waterbottle"
# t = "erbottlewat"  #output : True
t = "ejlkrbottlewat"  #output : False
s = s+s

isRotation = False
if s.find(t) != -1:
    isRotation = True

print(isRotation)