# list is given & if there is lowercse string avoid it. if no then add in ans string and if string is uppercase then add its value ( like A=1, B=2..) find total sum. 

list = [28, "AC" , "g", "h", "KM", "IPL", " RCB"]
#  = 28 + (1+2)

print(dir(list))


num = 0

n = len(list)
for item in range(n):
    if type(item) == int:
        num += item
    elif item.islower():
        continue
    elif item.isupper():
        for ch in item:
            num += ord(ch) - ord('A')+1


print(num)

