class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DLinkedList():
    def __init__(self):
        self.head = None

    
    def insert(self,pos,data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            return

        if pos == 1:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            return 
        
        else:
            temp = self.head
            i = 1
            while i != pos-1 and temp.next != None:
                i += 1
                temp = temp.next
            
            if temp.next == None:
                temp.next = newNode
                newNode.prev = temp
                return

            newNode.next = temp.next
            newNode.prev = temp
            temp.next.prev = newNode
            temp.next = newNode
            return


    def remove(self,pos):
        if self.head == None:
            return
        
        if pos == 1:
            if self.head.next != None:
                self.head.next.prev = None
            self.head = self.head.next
            return
        
        temp = self.head
        i = 1
        while i != pos-1 and temp.next != None:
            i += 1
            temp = temp.next
        
        if temp.next == None:
            return

        if temp.next.next == None:
            temp.next = None
        else:
            temp.next = temp.next.next
            temp.next.prev = temp
        
         

    def removeD(self,data):
        if self.head.data == data:
            if self.head.next != None:
                self.head.next.prev = None
            self.head = self.head.next
            return
        
        temp = self.head
        while temp.next != None and temp.next.data != data:
            temp = temp.next
        
        if temp.next == None:
            return
        else:
            temp.next = temp.next.next
        

        
    def updateD(self,data,newData):
        if self.head.data == data:
            self.head.data = newData
            return
        
        temp = self.head
        while temp != None and temp.data != data:
            temp = temp.next
        
        if temp == None:
            return

        temp.data = newData
    

    def update(self,pos,data):
        if pos == 1:
            self.head.data = data
            return
        
        temp = self.head
        i = 1
        while i != pos and temp.next != None:
            i +=1 
            temp = temp.next
        
        if temp.next == None:
            return
        
        temp.data = data
   


    def length(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count


    def lengthPrev(self):
        temp = self.head
        count = 0

        while temp.next != None:
            temp = temp.next

        while temp != None:
            count += 1
            temp = temp.prev
        
        return count


    def printll(self):
        temp = self.head
        while temp != None:
            print(temp.data , end="<--->")
            temp = temp.next
        print("None")







ll = DLinkedList()
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
ll.insert(3,300)
ll.printll()
# ll.insert(5,50)
# ll.printll()


# ll.remove(1)
# ll.remove(4)
# ll.remove(12)
# ll.remove(3)
# ll.printll()


# ll.insert(5,50)
# ll.insert(6,60)
# ll.printll()

# ll.removeD(50)
# ll.removeD(40)
# ll.removeD(10)
# ll.removeD(30)
# ll.printll()


# ll.updateD(40,400)
# ll.updateD(10,100)
# ll.updateD(50,500)
# ll.printll()


# ll.update(1,100)
# ll.update(4,400)
# ll.update(39,300)
# ll.printll()


print(ll.length())
print(ll.lengthPrev())