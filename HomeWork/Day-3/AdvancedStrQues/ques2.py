# Given a list of overlapping substrings, reconstruct the original string.  
# Input: ["abc", "bcd", "cde"] → Output: "abcde"

input = ["abc", "bcd", "cde", "fabc"]

# print(input)


s = ""

for i in range(len(input)):
    str = input[i]
    for ch in str:
        if ch not in s:
            s += ch


print(s)