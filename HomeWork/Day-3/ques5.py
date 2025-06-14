# check for substring rotation

#  Input: "waterbottle", "erbottlewat" → Output: True

s = "waterbottle"
# t = "erbottlewat"  #output : True
t = "erbottlewat"  #output : False
s = s+s 
# this also works: s= 2*s



# logic -1 --------------------------------------
# isRotation = False
# if s.find(t) != -1:
#     isRotation = True

# logic -2 --------------------------------------
if t in s:
    print("Yes")
else:
    print("No")

# print(isRotation)


