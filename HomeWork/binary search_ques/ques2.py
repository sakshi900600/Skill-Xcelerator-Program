#  Question: Given a sorted dictionary of valid medicine names, return the first word that starts with a given prefix. 

# 🧾 Input: 
#  meds = ["acinil", "aspirin", "azithromycin", "benadryl", "cetirizine"] 
#  prefix = "azi" 
#  ✅ Output: "azithromycin"


meds = ["acinil", "aspirin", "azipq", "azithromycin", "benadryl", "cetirizine"] 
prefix = "azi" 

# ans = azipq

def binary_search(li,key):
    si = 0
    ei = len(li)-1
    ans = ""

    while si <= ei:
        mid = (si+ei)//2

        if li[mid].startswith(prefix):
            ans = li[mid]
            ei = mid-1
        else:
            si = mid+1

    return ans



print(binary_search(meds,prefix))
