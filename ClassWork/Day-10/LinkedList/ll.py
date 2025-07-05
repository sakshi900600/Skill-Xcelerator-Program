class Node():
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    
    def insert(self,pos,data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            return

        if pos == 1:
            newNode.next = self.head
            self.head = newNode
            return 
        
        else:
            temp = self.head
            i = 1
            while i != pos-1 and temp.next != None:
                i += 1
                temp = temp.next

            newNode.next = temp.next
            temp.next = newNode
            return


    def remove(self,pos):
        if self.head == None:
            return
        
        if pos == 1:
            self.head = self.head.next
            return
        
        temp = self.head
        i = 1
        while i != pos-1 and temp.next != None:
            i += 1
            temp = temp.next
        
        temp.next = temp.next.next
        return
    

    def removeD(self,data):
        if self.head.data == data:
            self.head = self.head.next
            return
        
        temp = self.head
        while temp.next != None and temp.next.data != data:
            temp = temp.next
        
        temp.next = temp.next.next
        return

        
    def updateD(self,data,newData):
        if self.head.data == data:
            self.head.data = newData
            return
        
        temp = self.head
        while temp.data != data and temp != None:
            temp = temp.next
        
        temp.data = newData
        return
        
    def update(self,pos,data):
        if pos == 1:
            self.head.data = data
            return
        
        temp = self.head
        i = 1
        while i != pos and temp.next != None:
            i +=1 
            temp = temp.next
        
        temp.data = data
        return
        

    def length(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count


    def printll(self):
        temp = self.head
        while temp != None:
            print(temp.data , end="--->")
            temp = temp.next
        print("None")





ll = LinkedList()
ll.insert(1,10)
ll.printll()
ll.insert(2,20)
ll.printll()
ll.insert(3,30)
ll.printll()
ll.insert(4,40)
ll.printll()

# ll.insert(1,100)
# ll.printll()
# ll.insert(3,300)
# ll.printll()
# ll.insert(5,50)
# ll.printll()


ll.remove(4)
ll.printll()
# ll.remove(4)
# ll.printll()


# ll.insert(5,50)
# ll.insert(6,60)
# ll.printll()

# ll.removeD(50)
# ll.removeD(60)
# ll.removeD(10)
# ll.removeD(30)
# ll.printll()


# ll.updateD(40,400)
# ll.updateD(10,100)
# ll.updateD(30,300)
# ll.printll()


# ll.update(1,100)
# ll.update(4,400)
# ll.update(3,300)
# ll.printll()


print(ll.length())