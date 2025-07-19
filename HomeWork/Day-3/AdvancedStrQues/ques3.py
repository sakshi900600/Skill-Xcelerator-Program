# pattern based string validation
# Check whether a string follows a specific character pattern, like abba. 

#  Input: pattern = "abba", string = "dog cat cat dog" → Output: True 
#  Input: pattern = "abba", string = "dog cat cat fish" → Output: False



# My very simple funda: I did nothing. 
# Just store the (curr pattern -> curr str) in dct1 and (curr str -> curr pattern) in dct2 if not found else get values from both dict and compare if its not match then false otherwise true. 
# and It'd done ✅👏


# pattern = "abba"
# str = "dog cat cat dog"

pattern = "abba"
str = "dog dog dog dog"

li = str.split()
# print(len(li))


def word_pat(pattern, s):
    n = len(pattern)
    dct1 = {}
    dct2 = {}
    if len(pattern) != len(s):
        return False
    
    i = 0
    j = 0

    while i<n and j<n:
        p = pattern[i]
        st = s[j]

        if dct1.get(p) == None and dct2.get(st) == None:
            dct1[p] = st
            dct2[st] = p               
        else:
            d1 = dct1.get(p)
            d2 = dct1.get(st)

            if d1 != st and d2 != p:
                return False
        
        i += 1
        j += 1
    
    return True



print(word_pat(pattern, li))


