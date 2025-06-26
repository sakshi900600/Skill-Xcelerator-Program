#  Input: 
titles = ["Antibiotics 101", "Asthma Care", "Cardiology", "Covid Protocols", "Diabetes Guide"] 
prefix = "C" 
#  ✅ Output: ["Cardiology", "Covid Protocols"]


def binary_search(li,key):
    si = 0
    ei = len(li)-1
    ans = []

    while si <= ei:
        mid = (si+ei)//2

        if li[mid].startswith(key):
            ans.append(li[mid])
            si = mid +1
        else:
            ei = mid - 1

    return ans



ans = binary_search(titles,prefix)
print(ans)
