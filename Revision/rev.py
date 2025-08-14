# adj matrix:

n = 5 # no of nodes
adjmat = [[0]*n for _ in range(n)]

def add_edge_mat(i,j):
    adjmat[i][j] = 1
    adjmat[j][i] = 1


add_edge_mat(0,1)
add_edge_mat(0,3)
add_edge_mat(1,3)
add_edge_mat(1,2)
add_edge_mat(3,4)
add_edge_mat(2,4)

# print(adjmat)
# [[0, 1, 0, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 0, 1], [1, 1, 0, 0, 1], [0, 0, 1, 1, 0]]


# n = 5

# adjlist = [[]*n for _ in range(n)]

# def add_edge_list(i,j):
#     adjlist[i].append(j)
#     adjlist[j].append(i)

# add_edge_list(0,1)
# add_edge_list(0,3)
# add_edge_list(1,3)
# add_edge_list(1,2)
# add_edge_list(3,4)
# add_edge_list(2,4)

# print(adjlist)

# [[1, 3], [0, 3, 2], [1, 4], [0, 1, 4], [3, 2]]


from collections import deque

def bfs(root,n):
    visited = [0]*n
    q = deque()

    q.append(root)
    visited[root] = 1

    while q:
        node = q.popleft()
        print(node)

        # adjmat
        for i in range(n):
            if adjmat[node][i] == 1:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append(i)

        # adjlist
        # for x in adjlist[node]:
        #     if visited[x] == 0:
        #         visited[x] = 1
        #         q.append(x)


# maximum distance from given node:
def max_dis(root,n):
    visited = [0]*n
    q = deque()

    q.append(root)
    visited[root] = 1

    dist = [0]*n

    while q:
        node = q.popleft()

        for i in range(n):
            if adjmat[node][i] == 1:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append(i)
                    dist[i] = dist[node]+1
    
    print(max(dist))
    

# min jumps to reach at end:
# def min_jump(a):



# bfs(0,n)
# max_dis(0,n)
    