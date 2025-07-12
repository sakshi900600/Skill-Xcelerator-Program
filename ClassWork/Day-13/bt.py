class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

class BT:
    def __init__(self):
        self.root = None
    



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


def createBTFromInorder(node, li):
    si = 0
    ei = len(li-1)


# maxvalue in the tree
def maxValue(node):
    if node == None:
        return -100
    
    maxleft = maxValue(node.left)
    maxright = maxValue(node.right)

    return max(node.data, max(maxleft,maxright))


# height of a tree
def heightOfTree(node):
    if node == None:
        return 0
    
    left_height = heightOfTree(node.left)
    right_height = heightOfTree(node.right)

    return max(left_height,right_height)+1

    

# longest distance between 2 nodes
def longestDistance(node):
    if node == None:
        return 0
    
    longest_height_left = heightOfTree(node.left)
    longest_height_right = heightOfTree(node.right)

    maxi = 0
    return max(maxi,(longest_height_left + longest_height_right + 1))


# maximum width between 2 nodes on horizontal level:


 

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(35)
    root.left.left = Node(44)
    root.left.right = Node(51)
    root.right.right = Node(600)
    root.right.right.left = Node(60)
    root.right.right.right = Node(90)
    

# IOP(root)
# print("\n")
# POP(root)
# print("\n")
# PostOrder(root)


# print(maxValue(root))
# print(heightOfTree(root))
print(longestDistance(root))