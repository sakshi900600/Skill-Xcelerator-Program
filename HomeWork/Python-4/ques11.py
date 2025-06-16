#  Binary Search for Player Jersey Number

jerseys = [7, 10, 11, 14, 23, 30, 33] 
search = 23 

def findJersery(arr, key):
    si = 0
    ei = len(arr)-1

    while si <= ei:
        mid = (si+ei)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            si = mid+1
        else:
            ei = mid-1

    return -1


print(findJersery(jerseys, search))