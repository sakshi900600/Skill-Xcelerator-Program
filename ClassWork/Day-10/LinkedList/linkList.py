class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.length = 0


def insert(head,data,pos):
    newNode = Node(data)

    # start
    if head == None:
        head = newNode
        return head
    
    if pos == 1:
        newNode.next = head
        head = newNode
        return head

    else:
        temp = head
        i = 1
        while i != pos-1 and temp.next != None:
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode 
        return head

def remove(head,pos):
    if head == None:
        return head

    if pos == 1:
        head = head.next
        return head
    
    temp = head
    i = 1
    while i != pos-1 and temp.next != None:
        i += 1
        temp = temp.next

    temp.next = temp.next.next
    return head
 

def removeD(head,data):
    if head == None:
        return head
    
    if head.data == data:
        head = head.next
        return head
    
    temp = head
    while temp.next != None and temp.next.data != data:
        temp = temp.next

    if temp.next == None:
        return head
    
    temp.next = temp.next.next
    return head


def update(head,data,pos):
    if head == None:
        return head
    
    if pos == 1:
        head.data = data
        return head
    
    temp = head
    i = 1
    while i != pos and temp.next != None:
        i += 1
        temp = temp.next
    
    temp.data = data
    return head


def updateD(head,data,newdata):
    if head == None:
        return head
    
    if head.data == data:
        head.data = newdata
        return head
    
    temp = head
    while temp != None and temp.data != data:
        temp = temp.next

    temp.data = newdata
    return head


def printll(head):
    temp = head
    while temp != None:
        print(temp.data, end="--->")
        temp = temp.next
    print(None)

def length(head):
    temp = head
    count = 0
    while temp != None:
        count += 1
        temp = temp.next
    
    return count






head = None
# head = remove(head,20)

head = insert(head,10,1)
printll(head)
head = insert(head,20,2)
printll(head)
head = insert(head,30,3)
printll(head)
head = insert(head,40,2)
printll(head)
head = remove(head,3)
printll(head)
head = insert(head,50,1)
printll(head)

head = removeD(head,50)
printll(head)

head = updateD(head,10,100)
printll(head)
head = updateD(head,40,400)
printll(head)
head = updateD(head,30,300)
printll(head)

head = update(head,10,1)
printll(head)
head = update(head,40,2)
printll(head)
head = update(head,30,3)
printll(head)

head = update(head,30,3)
printll(head)

head = insert(head,50,4)
printll(head)

head = remove(head,4)
printll(head)

print("\nlength = ",length(head))