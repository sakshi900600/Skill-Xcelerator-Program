# ✅ 9. Celebrity Problem 
# Description: In a party of N people, a celebrity is known by everyone but knows no one. Find the 
# celebrity using a stack. 
# Input:
M = [ 
 [0, 1, 1], 
 [0, 0, 1], 
 [0, 0, 0] 
] 
 
# Output: 2

def celebrity1(M):

    r = len(M)
    c = len(M[0])

    iknow = [0]*r
    knowMe = [0]*c


    for i in range(r):
        for j in range(c):
            if M[i][j] == 1:
                iknow[i] += 1
                knowMe[j] += 1


    for i in range(r):
        if iknow[i]==0 and knowMe[i]==r-1:
            return i
    
    return -1


# print(celebrity1(M))


def celebrity2(M):
    jl