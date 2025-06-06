# palindrome check

str = "abffba"


si=0
ei=len(str)-1
isPalindrome = True

while si<ei:
    if str[si] != str[ei]:
        isPalindrome = False
        break
    si += 1
    ei -= 1


print(isPalindrome)