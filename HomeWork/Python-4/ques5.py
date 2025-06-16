# Task: Use binary search to find the index of the goal scored. 


goals = [2, 5, 8, 10, 13, 18, 20] 
search_goal = 50
 
#  Output: 
# Goal found at index: 3 

def binarySearch(arr, key):
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


print(binarySearch(goals, search_goal))