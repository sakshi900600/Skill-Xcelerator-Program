# highest value palindrome:
# given a string of no and an integer value k. you can only perform k operations/changes in the given string such that that string become a palindrome and through this you need to find the largest palindrom value and return it: 

# example: 
# s = "1231" 
# k=3
# Make 3 replacements to get "9339".

s = "12321"
k=1
# Make 1 replacement to get "12921".


def highValPalindrome(s,k):
    s = list(s)
    n = len(s)
    mark = [0] * n

    l = 0
    r = n-1

    # first making string palindrome
    while l <= r:
        if s[l] != s[r]:
            if s[l] > s[r]:
                s[r] = s[l]
                mark[r] = 1
            else:
                s[l] = s[r]
                mark[l] = 1
            k -= 1
        l += 1
        r -= 1
    

    if k < 0:
        return "-1"
    

    # making palindromic string value highest
    l = 0
    r = n-1

    while l<=r:
        # mid index
        if l==r and k>=1:
            s[l] = '9'
            break

        if s[l] < '9': 
            if mark[l]==0 and mark[r] == 0 and k>=2:
                s[l] = s[r] = '9'
                k -= 2

            if (mark[l]==1 or mark[r]==1) and k>=1:
                s[l] = s[r] = '9'
                k -= 1
        l += 1
        r -= 1

    return "".join(s)



print(highValPalindrome(s,k))