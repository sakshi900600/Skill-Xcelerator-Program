# Write a function that finds the longest prefix of a given word that exists in the list.

# 🧾 Input: 
diseases = ["aids", "allergy", "anemia", "asthma", "autism"] 
query = "autistic" 

#  ✅ Output: "autism"


def binary_search(li,key):
    si = 1
    ei = len(key)
    ans = ""

    while si <= ei:
        mid = (si+ei)//2

        prefix = key[:mid]

        isFound = False
        for item in li:
            if item.startswith(prefix):
                ans = item
                isFound = True
                break
        
        if isFound:
            si = mid+1
        else:
            ei = mid-1
    
    return ans


matched_prefix = binary_search(diseases, query)

print(matched_prefix)



