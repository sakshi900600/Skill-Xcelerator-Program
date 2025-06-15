# Count and print the total number of vowels


# Output: 11
s = "Einstein had a creative mind"
s = s.lower()
vowels = {"a", "e","i","o","u"}

count  = 0
for i in range(len(s)):
    if s[i] in vowels:
        count += 1
        print(s[i])

print(count)
