
arr = [1,2,3,4,5]
d = 4


def rotLeft(a, d):
    # Write your code here
    n = len(a)
    newarr = []
    
    for i in range(len(a)):
        index = (i-d+n)%n
        newarr.insert(index,a[i])
        
    return newarr


print(rotLeft(arr,d))