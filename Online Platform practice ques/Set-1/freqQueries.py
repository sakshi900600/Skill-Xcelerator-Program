

queries = [(1,1),(2,2),(3,3),(1,1),(1,1),(2,1),(3,2)]
# queries = [(3,4),(2,1003),(1,16),(3,1)]

def freqQuery1(queries):
    dct = {}

    for i in range(len(queries)):
        query = queries[i][0]
        data = queries[i][1]

        if query == 1:
            dct[data] = dct.get(data,0)+1
        
        elif query == 2:
            dct[data] = dct.get(data,0)-1
        
        elif query == 3:
            result = 0
            for key,val in dct.items():
                if val == data:
                    result = 1
            print(result)

# freqQuery1(queries)

# this first approach works good for small inputs but in the 3 query we are traversing whole dict everytime which takes lots of time that's why some test case doesn't pass. 



# Solution:  

