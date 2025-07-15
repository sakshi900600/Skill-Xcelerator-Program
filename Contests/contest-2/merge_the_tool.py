# Sample Input

# STDIN       Function
# -----       --------
# AABCAAADA   s = 'AABCAAADA'
# 3           k = 3

# Sample Output
# AB
# CA
# AD

# take k char from strting and then print unique char string.


def merge_the_tools(string, k):
    # your code goes here
    count = 0
    str = ""
    
    for i in string:
        if i not in str:
            str += i
            
        count += 1
        if count == k:
            print(str)
            count = 0
            str = ""
            