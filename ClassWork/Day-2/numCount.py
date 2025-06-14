# s = "228255855854441333" # output: 2, 8, 4, 
s = "1223333455666666"  # output: 3, 4, 5, 

# Count how many times each digit appears
# from collections import Counter
# freq = Counter(t)

# Check which digit does NOT appear as many times as its value
# for digit in freq:
#     if freq[digit] != int(digit):
#         print(digit, end=", ")


li = list()
for i in range(len(s)):
    freq = s.count(s[i])
    if(freq != int(s[i])):
        if(li.count(s[i]) == 0):
            li.append(s[i])

print(li)