# Task: Return the word with the highest number of unique letters.

# output: 'photosynthesis' with 9 unique characters

# words = ["photosynthesis", "respiration", "chlorophyll", "transpiration"] 
words = ["Mango", "Apple", "Banana", "Grapes"]
 

def finduniqueLetter(str):
    count = 0
    s = ""
    for i in range(len(str)):
        if str[i] not in s:
            s += str[i]
            count += 1

    return count

    


maxcount = 0
maxElem = ""

for i in range(len(words)):
    str = words[i]
    curr_count = finduniqueLetter(str)
    if curr_count > maxcount:
        maxcount = curr_count
        maxElem = str


print(f"{maxElem} with {maxcount} uniques characters")
