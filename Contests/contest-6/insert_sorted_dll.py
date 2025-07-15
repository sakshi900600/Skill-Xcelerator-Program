def sortedInsert(llist, data):
    # Write your code here
    newNode = DoublyLinkedListNode(data)
    
    if llist == None:
        return newNode
    
    if llist.data >= data:
        newNode.next = llist
        llist.prev = newNode
        llist = newNode
        return llist
    
    temp = llist
    while temp.next != None and temp.next.data < data:
        temp = temp.next

    
    newNode.next = temp.next
    newNode.prev = temp
    if temp.next != None:
        temp.next.prev = newNode
    temp.next = newNode
    
    return llist
    