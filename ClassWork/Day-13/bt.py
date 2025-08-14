class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

# inorder traversal : left-root-right
def IOP(node):
    if node == None:
        return
    IOP(node.left)
    print(node.data,end=" ")
    IOP(node.right)



# preorder traversal:  root-left-right
def POP(node):
    if(node == None):
        return
    
    print(node.data,end=" ")
    POP(node.left)
    POP(node.right)


# postorder traversal: 
def PostOrder(node):
    if(node == None):
        return
    
    PostOrder(node.left)
    PostOrder(node.right)
    print(node.data,end=" ")


# maxvalue in the tree
def maxValue(node):
    if node == None:
        return -100
    
    maxleft = maxValue(node.left)
    maxright = maxValue(node.right)

    return max(node.data, max(maxleft,maxright))


# minvalue in the tree
def minValue(node):
    if node == None:
        return 1000
    
    minleft = minValue(node.left)
    minright = minValue(node.right)

    return min(node.data, min(minleft,minright))



# height of a tree
def heightOfTree(node):
    if node == None:
        return 0
    
    left_height = heightOfTree(node.left)
    right_height = heightOfTree(node.right)

    return max(left_height,right_height)+1

    

# longest distance between 2 nodes - diameter
 
def longestDistance(node):
    global maxi
    maxi = 0
    if node == None:
        return 0
    
    longest_height_left = heightOfTree(node.left)   
    longest_height_right = heightOfTree(node.right)
    maxi = max(maxi, (longest_height_left + longest_height_right))

    return maxi


# maximum width between 2 nodes on horizontal level:

def hd_helper(root,hd):
    global min_hd, max_hd
    if root == None:
        return

    min_hd = min(min_hd, hd)
    max_hd = max(max_hd, hd)

    hd_helper(root.left, hd-1)
    hd_helper(root.right, hd+1)


min_hd = 0
max_hd = 0


def horizontal_distance(root):
    global min_hd, max_hd
    min_hd = 0
    max_hd = 0
    hd_helper(root,0)

    return max_hd - min_hd

    


# create binary tree from given list - iterative
def create_bt_it(li):

    if not li:
        return None
    
    nodes = []
    for i in li:
        if i == -1:
            nodes.append(None)
        else:
            nodes.append(Node(i))
    
    # print(nodes)

    for i in range(len(li)):
        if nodes[i] is not None:
            left_idx = 2*i+1
            right_idx = 2*i+2

            if left_idx < len(li):
                nodes[i].left = nodes[left_idx]
            
            if right_idx < len(li):
                nodes[i].right = nodes[right_idx]
    
    return nodes[0]
        

# create binary tree from given list - recursive
def create_bt_rec(li,index):
    # if invalid index or -1
    if index >= len(li) or li[index] == -1:
        return None

    node = Node(li[index])
    node.left = create_bt_rec(li,2*index+1)
    node.right = create_bt_rec(li,2*index+2)

    return node




# top-view of a tree:
from collections import deque
# queue = deque()

def top_view(root):
    if root == None:
        return []
     
    dct = {}
    q = deque([(root,0)])

    while q:
        node, hd = q.popleft()

        if hd not in dct:
            dct[hd] = node.data
        
        if node.left != None:
            q.append((node.left,hd-1))
        
        if node.right != None:
            q.append((node.right,hd+1))
    

    sorted_key = sorted(dct.keys())
    for i in sorted_key:
        print(dct[i], end=" ")



def bottom_view(root):
    if root == None:
        return
    
    dct = {}
    q = deque([(root,0)])

    while q:
        node, hd = q.popleft()

        dct[hd] = node.data

        if node.left != None:
            q.append((node.left, hd-1))
        
        if node.right != None:
            q.append((node.right, hd+1))
    

    sortedKeys = sorted(dct.keys())

    for i in sortedKeys:
        print(dct[i])



# left view:
def left_view(root,level,li):
    if root == None:
        return
    
    if level == len(li):
        li.append(root.data)
    
    left_view(root.left, level+1, li)
    left_view(root.right, level+1, li)


# right view:
def right_view(root,level,li):
    if root == None:
        return
    
    if level == len(li):
        li.append(root.data)
    
    right_view(root.right, level+1, li)
    right_view(root.left, level+1, li)





# ----------------- Boundary traversal ------------------ #

def isleaf(root):
    return root.left == None and root.right == None

def addLeftBoundary(root,li):
    curr = root

    while curr:
        if not isleaf(curr):
            li.append(curr.data)
        
        if curr.left != None:
            curr = curr.left
        else:
            curr = curr.right


def addRightBoundary(root,li):
    curr = root
    temp = []

    while curr:
        if not isleaf(curr):
            li.append(curr.data)
        
        if curr.right != None:
            curr = curr.right
        else:
            curr = curr.left


def addleaves(root,li):
    if root == None:
        return
    
    if isleaf(root):
        li.append(root.data)
        return
    
    addleaves(root.left,li)
    addleaves(root.right,li)


def print_boundary_traversal(root,li):
    if root == None:
        return
    
    if not isleaf(root):
        li.append(root.data)
    
    addLeftBoundary(root.left,li)
    addleaves(root,li)
    addRightBoundary(root.right,li)

    return li


# ---------------------    bt    -------------------------  #





# ----------------------------------------------------------











if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(35)
    root.left.left = Node(44)
    root.left.right = Node(51)
    root.right.right = Node(600)
    # root.right.right.left = Node(60)
    # root.right.right.right = Node(90)
    

# IOP(root)
# print("\n")
# POP(root)
# print("\n")
# PostOrder(root)

# print(maxValue(root))
# print(minValue(root))

# print(heightOfTree(root))
# print(longestDistance(root))


# print(horizontal_distance(root))


# li = [2,9,8,10,11,-1,12]
# IOP(create_bt_it(li))
# IOP(create_bt_rec(li,0))



# top_view(root)
bottom_view(root)

# li = []
# left_view(root,0,li)
# right_view(root,0,li)
# print(li)




# boundary traversal
# li = []
# print_boundary_traversal(root,li)
# print(li)