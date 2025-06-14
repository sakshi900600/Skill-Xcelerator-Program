# Sort a string by placing all letters before digits, keeping original relative order.  
# Input: "a1b2c3d4" → Output: "abcd1234"


s = "a1b2c3d4"

alpha = ""
num = ""

for ch in s:
    if ch.isdigit():
        num += ch
    if ch.isalpha():
        alpha += ch


final_ans = alpha + num
print(final_ans)