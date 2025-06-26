# # Find Maximum Length of Common Prefix in Sorted Names

# # 🧾 Input: 
# #  names = ["Ankit", "Ankur", "Ansh", "Anya"] 
# #  ✅ Output: 3 (from "Ank") 


# names = ["Ankit", "Ankur", "Ansh", "Anya"] 
# # names.sort(key=len)
# # print(names)


# nfirst = names[0]
# nlast = names[len(names)-1]

# count = 0
# for i in range(len(nfirst)):
#     if nfirst[i] == nlast[i]:
#         count += 1
#     else:
#         break


# print(count)





titles = ["Antibiotics 101", "Asthma Care", "Cardiology", "Covid Protocols", "Diabetes Guide"] 
prefix = "C" 

#  ✅ Output: ["Cardiology", "Covid Protocols"]

def binary_search(arr,target):
    li = []
    si = 0
    ei = len(arr)-1

    while si <= ei:
        mid = (si+ei)//2

        word = arr[mid]
        if word[0] == target:
            li.append(word)
        elif arr[mid] < target:
            si = mid+1
        else:
            ei = mid-1
        
    return li



li = binary_search(titles,prefix)
print(li)