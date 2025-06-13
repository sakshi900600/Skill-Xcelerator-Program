# count and print freq of elem in list

li = [1,2,3,"abc","abc", "abc" , True ]



for i in range(len(li)):
    freq = li.count(i)
    print(freq, li[i])
