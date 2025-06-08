# s = "ABACDDCDXYBAGHGGHGABYXDCDDCABA"
s = "ABCCBA"
length = len(s)
count = 0


# AT LAST store in the list instead of printing if it is not in the map and at last return the length of the list.


# case - 1
for i in range(length):
    for j in range(i, length):
        subStr = s[i:j+1]
        if subStr == subStr[::-1]:
            # print(subStr)
            count += 1


# case - 2
# for i in range(length):
#     for j in range(i+1, length+1):
#         subStr = s[i:j+1]
#         if subStr == subStr[::-1]:
#             print(subStr)
#             count += 1



# # case - 3
# for i in range(length):
#     for j in range(i, length):
#         subStr = s[i:j]
#         if subStr == subStr[::-1]:
#             print(subStr)
#             count += 1


print(count)
