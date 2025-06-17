# decode nested encoded string: 
#  Implement a decoder that can handle nested encoding rules of the form k[encoded_string], 
# where k is a number and encoded_string is repeated k times.  

# Input: "3[a2[c]]" → Output: "accaccacc"

# s = "ab"
# print(3*s)


s = "3[a2[c]]"


def decodeString(s):
    stack = []
    current_num = 0
    current_str = ""
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char
    
    return current_str

# Test the function
print(decodeString("3[a2[c]]"))  # Output: "accaccacc"


