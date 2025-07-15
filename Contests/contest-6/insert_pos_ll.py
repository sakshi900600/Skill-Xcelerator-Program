def insertNodeAtPosition(llist, data, position):
    # Write your code here
    newNode = SinglyLinkedListNode(data)
    temp = llist
    cnt = 0
    while cnt != position-1 and temp.next != None:
        cnt += 1
        temp = temp.next

    newNode.next = temp.next
    temp.next = newNode
    return llist
        
    