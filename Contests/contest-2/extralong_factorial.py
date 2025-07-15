def extraLongFactorials(n):
    # Write your code here
    if n==1:
        return 1
    
    return n * extraLongFactorials(n-1)


n = 25

print(extraLongFactorials(n))



