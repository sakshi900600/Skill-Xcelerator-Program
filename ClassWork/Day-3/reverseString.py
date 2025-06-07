s = "abcd"

reversed_str = ""

i= len(s)-1

while i >= 0:
    reversed_str += s[i]
    i -= 1


rev_str = ""
for x in s:
    rev_str = x + rev_str
    

print(reversed_str)
print(rev_str)


# 
gretting = "Hello, World!"
print(gretting[0 :-1])
print(gretting[::-1]) # to reverse a string. 



