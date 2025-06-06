s = "228255855854441333" # output: 2, 8, 4, 
t = "1223333455666666"  # output: 3, 4, 5, 

# Count how many times each digit appears
from collections import Counter
freq = Counter(t)

# Check which digit does NOT appear as many times as its value
for digit in freq:
    if freq[digit] != int(digit):
        print(digit, end=", ")
