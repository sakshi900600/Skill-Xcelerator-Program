# ques 1
friends_ages = {

    "Mickey": 12,
    "Minnie": 23,
    "Donald": 33,
    "Goofy" : 34
}

# ques 2
# friends_ages["Pluto"] = 5
# print(friends_ages)


# ques 3
# print(friends_ages["Donald"])

# ques 4
# friends_ages.pop("Goofy")
# del friends_ages["Goofy"]
# print(friends_ages)


# ques 5
# print(friends_ages.keys())

# ques 6
# print(friends_ages.values())


# ques 7
friends_ages["Minnie"] = 29

# ques 8
# print(len(friends_ages))

# ques 9
# for name, age in enumerate(friends_ages):

# for key,value in friends_ages.items():
    # print(f"{key} is {value} years old ")


# ques 10
li = friends_ages.items()
# print(li)


#ques 11
# if "Daisy" in friends_ages:
#     print("yes")
# else:
#     print("No")


# ques 12

if "Daisy" not in friends_ages:
    friends_ages["Daisy"] = 25

# print(friends_ages)


# ques 13
# party_guests = friends_ages.copy()

# ques 14
mickey_info = {
    "age" : 12,
    "pet" : "Pluto",
    "hobbies": ["magic", "dancing"]
}

# ques 15
# friends_ages.clear()


# ques 16
print(friends_ages["Max"])
friends_ages.get("Max")


# ques 17
# names = ["Mickey", "Donald", "Goofy"] 
# ages = [27, 30, 32]

# dct = dict(zip(names, ages))
# print(dct)


# ques 18
# dct = dict(zip(ages, names))
# print(dct)


# ques 19
# maxAge = 0
# maxAgeElem = ""

# for key,value in dct.items():
#     if value > maxAge:
#         maxAge = value
#         maxAgeElem = key

# print(maxAgeElem)
# print(maxAge)


# ques 20
# birthday_Countdown = {
#     "Minne" : 45,
#     "Anu" :  21,
#     "Sakshi" : 123
# }