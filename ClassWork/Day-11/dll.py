class Node():
    def __init__(self,data):
        self.data = data 
        self.prev = None
        self.next = None


class Dll():
    def __init__(self):
        self.head = None
    
    def insert(self,pos,data):
        newNode = Node(data)
        if pos == 1:
            if self.head == None:
                self.head = newNode
                return
            else:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode

        else:
            count = 1
            temp = self.head
            while temp.next != None and count < pos-1:
                temp = temp.next
                count += 1
            
            if temp.next == None:
                temp.next = newNode
                newNode.prev = temp
            else:
                newNode.next = temp.next
                newNode.prev = temp
                temp.next.prev = newNode
                temp.next = newNode


    def remove(self, pos):
        if self.head == None:
            return
        
        if pos == 1:
            if self.head.next == None:
                self.head = None
            self.head = self.head.next
            self.head.prev = None
        
        else:
            temp = self.head
            count = 0
            while temp.next != None and count < pos-1:
                temp = temp.next
                count += 1
            
            if temp.next.next == None:
                temp.next = None
            
            
        


        
    def printdll(self):
        temp = self.head
        next_str = ""
        while temp != None:
            next_str += str(temp.data) + "--->"
            if temp.next == None:
                break
            temp = temp.next

        print(next_str, "None")

        prev_str = ""
        while temp != None:
            prev_str += str(temp.data) + "<---"
            temp = temp.prev

        print(prev_str, "None")









dll = Dll()
dll.insert(1,1)
dll.insert(2,2)
dll.insert(3,3)
dll.insert(1,10)
dll.insert(5,50)
dll.insert(2,20)


            
dll.printdll()


                