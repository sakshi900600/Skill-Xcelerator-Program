# Find First Faulty Vaccine Batch ID

versions = ["v1.0", "v1.1", "v1.2", "v1.3", "v1.4"] 
target = "v1.3" 
#  ✅ Output: "v1.3"

def first_faulty(versions, target):
    
    l = 0
    r = len(versions)-1

    while l <= r:
        mid = (l+r)//2
        if versions[mid] == target:
            return target
        elif versions[mid] < target:
            l = mid+1
        else:
            r = mid-1

    return -1


print(first_faulty(versions, target))