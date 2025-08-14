# A		rotate 
# [1,6,5,2,4,3]	[6,5,2]
# [1,5,2,6,4,3]	[5,2,6]
# [1,2,6,5,4,3]	[5,4,3]
# [1,2,6,3,5,4]	[6,3,5]
# [1,2,3,5,6,4]	[5,6,4]
# [1,2,3,4,5,6]

# YES


# if by doing left rotation array can be sorted then print Yes else No 

# We will use inversion (count of elem greater than curr elem in left side). 
# if inversion is even then print yes else no

A = [1,3,4,2]
A = [1,2,3,5,4]

def larrysArray(A):
    # Write your code here
    count = 0
    n = len(A)
    
#     counting inversions 
    for i in range(n):
        for j in range(i):
            if A[j] > A[i]:
                count += 1
    
    if count % 2 == 0:
        return "YES"
    else:
        return "NO"
    


print(larrysArray(A))

