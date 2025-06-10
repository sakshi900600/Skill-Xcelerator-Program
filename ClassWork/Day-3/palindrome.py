# s = "ABACDDCDXYBAGHGGHGABYXDCDDCABA"



# AT LAST if it is not in the list,  store in the list instead of printing  and at last return the length of the list.


# print(dir(list))
# print(dir(set))

# case - 1  #output - 6 ------------------------  right ✅

s = "ABCCBA"
length = len(s)

set = set()
list = list()
for i in range(length):
    for j in range(i, length):
        subStr = s[i:j+1]
        if subStr == subStr[::-1]:
            # print(subStr)
            if(list.count(subStr) == 0):
                list.append(subStr)
            set.add(subStr)


print(list)
print(set)




# case - 2  # Output - 7
# set = set()
# list = list()
# for i in range(length):
#     for j in range(i, length+1):
#         subStr = s[i:j]
#         if subStr == subStr[::-1]:
#             # print(subStr)
#             if(list.count(subStr) == 0):
#                 list.append(subStr)
#             set.add(subStr)


# print(list)
# print(set)




# # case - 3   #output - 4
# set = set()
# list = list()
# for i in range(length):
#     for j in range(i+1, length+1):
#         subStr = s[i:j+1]
#         if subStr == subStr[::-1]:
#             # print(subStr)
#             if(list.count(subStr) == 0):
#                 list.append(subStr)
#             set.add(subStr)


# print(list)
# print(set)



# # case - 4   #output - 3
# set = set()
# list = list()
# for i in range(length):
#     for j in range(i+1, length):
#         subStr = s[i:j+1]
#         if subStr == subStr[::-1]:
#             # print(subStr)
#             if(list.count(subStr) == 0):
#                 list.append(subStr)
#             set.add(subStr)


# print(list)
# print(set)




print(len(list))
print(len(set))
