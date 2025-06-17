# Binary Search to Find Closest Goal Number 


goals = [3, 6, 9, 14, 18] 
search = 11 
 
# output: Closest goal: 9

def closestGoal(arr,key):
    si = 0
    ei = len(arr)-1

    closest = arr[0]

    while si <= ei:
        mid = (si+ei)//2

        if(abs(arr[mid]-key) < abs(closest-key)):
            closest = arr[mid]
        elif abs(arr[mid]-key) == abs(closest-key):
            closest = min(arr[mid], closest)

        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] < key:
            si = mid+1
        else:
            ei = mid-1
    return closest


print(closestGoal(goals, search))
