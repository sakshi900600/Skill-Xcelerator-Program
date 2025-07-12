

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next



# here only have to insert in anywhere in middle at the given position. So only this thing is handled in this function. 

# Note -> insert at head/tail is not handled in this fun. 

def insertNodeAtPosition(llist, data, position):
    # Write your code here
    if llist == None:
        return 
    newNode = SinglyLinkedListNode(data)
    i = 0
    temp = llist
    while i != position-1 and temp.next != None:
        i += 1
        temp = temp.next
    
    newNode.next = temp.next
    temp.next = newNode
    return llist
    
    