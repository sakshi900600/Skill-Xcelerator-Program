def rotateLeft(d, arr):
    # Write your code here
    n = len(arr)
    ans = []
    
    for i in range(n):
        index = (i+n-d) % n
        ans.insert(index,arr[i])
    
    return ans