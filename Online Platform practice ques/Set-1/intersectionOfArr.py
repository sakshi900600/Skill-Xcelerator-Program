# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.


num1 = [1,2,2,1]
num2 = [2,2]

ansSet = set()
for i in num1:
    if num1[i] in num2:
        ansSet.add(num1[i])


print(ansSet)