# graph
# directed and unddirected

# graph representation: adjacency matrix & list

# adjacency matrix:
n = 5
# matrix = [[0]*n for i in range(n)]
matrix = [[0]*(n) for _ in range(n)]

def add_edge(i,j):
    matrix[i][j] = 1
    matrix[j][i] = 1

# add_edge(1,2)
# add_edge(1,3)
# add_edge(1,4)
# add_edge(2,5)
# add_edge(2,6)
# add_edge(3,6)

# print(matrix)



# adjacency list:
# n = 6
# adjlist = [[]*n for _ in range(n+1)]

# def add_edge(i,j):
#     adjlist[i].append(j)
#     adjlist[j].append(i)

# add_edge(1,2)
# add_edge(1,3)
# add_edge(1,4)
# add_edge(2,5)
# add_edge(2,6)
# add_edge(3,6)

# print(adjlist)




# creating graph

add_edge(0,1)
add_edge(0,3)
add_edge(1,3)
add_edge(1,2)
add_edge(3,4)
add_edge(2,4)

# print(matrix)


from collections import deque

def bfs(root_node,n):
    visited = [False]*n
    q = deque()

    q.append(root_node)
    visited[root_node] = 1
    print(root_node)

    while q:
        node = q.popleft()

        # adj matrix
        for i in range(n):
            if matrix[node][i] == 1:
                if visited[i] == False:
                    visited[i] = True
                    q.append(i)
                    print(i)


        # adj list
        # for x in adjlist[node]:
        #     if visited[x] == False:
        #         visited[x] = True
        #         q.append(x)
        #         print(x)



# maximum node distance from given node
def max_dist(root_node,n):
    visited = [False]*n
    dist = [0]*n
    q = deque()

    q.append(root_node)
    visited[root_node] = True
    
    while q:
        node = q.popleft()

        for i in range(n):
            if matrix[node][i] == 1:
                if visited[i] == False:
                    visited[i] = True
                    q.append(i)
                    dist[i] = dist[node] + 1

    # print(dist)
    print(max(dist))




# min jumps to reach at end:
# 1 create graph

def min_jumps(a):
    n = len(a)

    # store arr elem 
    dct = {}
    for i in range(n):
        if a[i] in dct:
            dct[a[i]].append(i)
        else:
            dct[a[i]] = [i]
    
    # print(dct)

    q = []
    visited = [False]*n
    distance = 0

    q.append(0)

    while len(q) > 0:
        size = len(q)

        for i in range(size):
            curr_idx = q[0]
            q.pop(0)

            if curr_idx == n-1:
                return distance
            
            # next
            if curr_idx+1 < n and visited[curr_idx+1] == False:
                q.append(curr_idx+1)
                visited[curr_idx+1] = True
            
            # prev
            if curr_idx-1 >=0 and visited[curr_idx-1] == False:
                q.append(curr_idx-1)
                visited[curr_idx-1] = True
            
            # same value:
            li = dct[a[curr_idx]]
            for x in range(len(li)):
                if li[x] == False:
                    q.append(li[x])
                    visited[li[x]] = True
                    distance += 1




a = [100,-23,-23,404,100,23,23,23,3,404]
print(min_jumps(a))







bfs(0,5)
# max_dist(0,5)

# a = [ 7,6,9,7,9,6,9,7]
# min_jumps(a)