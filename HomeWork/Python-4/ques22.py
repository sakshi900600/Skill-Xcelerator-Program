# Binary Search to Find Closest Goal Number 


goals = [3, 6, 9, 14, 18] 
search = 13 
 
# output: Closest goal: 14

def closestGoal(arr,key):
    si = 0
    ei = len(arr)-1

    ans = -1
    while si <= ei:
        mid = (si+ei)//2
        if arr[mid] == key:
            ans = mid
            return ans
        elif arr[mid] < key:
            ans = mid
            si = mid+1
        else:
            ei = mid-1
    return ans


print(closestGoal(goals, search))
