from collections import deque

def topView(root):
    #Write your code here
    if root == None: 
        return []
    
    dct = {}
    q = deque([(root,0)])
    
    while q:
        node, hd = q.popleft()
        
        if hd not in dct:
            dct[hd] = node
        
        if node.left != None:
            q.append((node.left,hd-1))
        
        if node.right != None:
            q.append((node.right, hd+1))
            
    
    # sort the dictionary to print top-view correctly
    sorted_keys = sorted(dct.keys())
    for i in sorted_keys:
        print(dct[i], end=" ")
    
        