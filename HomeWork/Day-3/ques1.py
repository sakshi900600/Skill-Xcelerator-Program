# swap the first and last characters
# s = "python" output = "nythop"


def swapfltry(s):
    newStr = ""
    length = len(s)
    for i in range(length):
        if len(s) < 2:
            return s
        if i==0:
            newStr += s[len(s)-1]
        elif i==len(s)-1:
            newStr += s[0]
        else:
            newStr += s[i]
    return newStr


s = "python"  #output: "nython"
t = "Sakshi"  #output: "iakshS"
print(swapfltry(s))
print(swapfltry(t))


