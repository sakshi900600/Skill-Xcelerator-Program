# 

# arr = [4,5,6,7,0,1,2] # 0
arr = [11,13,15,17]

def findmin(arr):
    si = 0
    ei = len(arr)-1
    minelem = arr[0]

    while si <= ei:
        mid = (si+ei)//2
        if arr[si] <= arr[mid]: #left sorted
            minelem = min(minelem, arr[si])
            si = mid+1

        else:
            minelem = min(minelem, arr[mid])
            ei = mid-1
        
    return minelem


print(findmin(arr))