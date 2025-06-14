# how many times string is being used in the dict as key and value 

a = {
    "abc": "def",
    "abc" : "abc",
    "ghi" : "def",
    "def" : "abc"
}

#outpt: 
# {
#     "abc" : [("key" : 2), ("abc": 1)],
#     "def" : [("key" : 2), ("abc": 1)],
#     "ghi" : [("key" : 2), ("abc": 1)]
# }


key_list = list(a.keys())
value_list = list(a.values())

# print(key_list)
# print(value_list)

ans = {}
for i in range(len(key_list)):
    ans[i] = 0

print(ans)



for i in range(len(value_list)):
    str = value_list[i]
    freq = 0
    if value_list[i] == str:
        freq += 1
        ans[str] = freq

# print(ans)







