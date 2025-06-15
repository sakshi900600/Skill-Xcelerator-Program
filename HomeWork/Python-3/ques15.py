# Print characters from the string whose ASCII value is even

# Output: ['b', 'l']
# s = "biology"

s = "sakshi"


print(ord('g'))

for ch in s.lower():
    if ord(ch) % 2 == 0:
        print(ch)