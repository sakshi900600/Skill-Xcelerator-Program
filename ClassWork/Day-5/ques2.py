# # how many times string is being used in the dict as key and value 

# a = {
#     "abc": "def",
#     "abc" : "abc",
#     "ghi" : "def",
#     "def" : "abc"
# }

# #outpt: 
# # {
# #     ghi: [('key', 1), ('value', 0)]
# #     def: [('key', 1), ('value', 1)]
# #     abc: [('key', 1), ('value', 2)]
# # }



a = {
    "abc": "def",
    "abc": "abc",
    "ghi": "def",
    "def": "abc"
}

# Step 1: Count how many times each string is used as key and value
key_count = {}
value_count = {}

for key, value in a.items():
    if key in key_count:
        key_count[key] += 1
    else:
        key_count[key] = 1

    if value in value_count:
        value_count[value] += 1
    else:
        value_count[value] = 1


# print(key_count)
# print(value_count)

# Step 2: Get all unique strings involved
all_strings = set()

for k in key_count:
    all_strings.add(k)
for v in value_count:
    all_strings.add(v)

# print(all_strings)

# Step 3: Build the result dictionary
result = {}

for s in all_strings:
    if s in key_count:
        key_ct = key_count[s]
    else:
        key_ct = 0

    if s in value_count:
        val_ct = value_count[s]
    else:
        val_ct = 0
        
    result[s] = [("key", key_ct), ("value", val_ct)]

# print(result)

# Step 4: Print the result

for k, v in result.items():
    print(f"{k}: {v}")


