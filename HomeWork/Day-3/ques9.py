# longest substring without repeatig characters
#  Input: "abcabcbb" → Output: 3 (substring: "abc")

s  = "abcabcbb"

# find substring & add in set (to avoid duplicate) then traverse set & for each value call fun that will return true if its all char freq is 1 .
# take a max var & whatever the valid substr is stored the maxleng & maxlen substr

substrings = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        substr = s[i : j+1]
        substrings.add(substr)

print(substrings)


def validation(s):
    charCount = dict()

    for char in s:
        charCount[char] = charCount.get(char,0)+1
    
    print(charCount)

    for char, count in charCount.items():
        if count > 1:
            return False

    return True



maxLen = 0
maxLenSubstr = ""
for item in substrings:
    if(validation(item) == True):
        if len(item) > maxLen:
            maxLen = len(item)
            maxLenSubstr = item

print(maxLen)
print(maxLenSubstr)