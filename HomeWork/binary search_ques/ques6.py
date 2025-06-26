

drugs = [ 
  ["amox", "azith", "cefix"], 
  ["doxy", "ibupro", "levo"], 
  ["metro", "parace", "sulfa"] 
] 
target = "levor" 


def binary_search(arr,target):
    si = 0
    ei = len(arr)-1

    while si <= ei:
        mid = (si+ei)//2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            si = mid+1
        else:
            ei = mid-1
        
    return False


result = False
for li in drugs:
    # print(li)
    result = binary_search(li,target)
    if result != False:
        break

print(result)
