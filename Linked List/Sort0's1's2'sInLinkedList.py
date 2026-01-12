class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertAtBeg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
        if self.tail is None:
            self.tail = new_node
        
    def insertAtLast(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            self.tail.next = new_node
            self.tail = new_node
            
            
    def insertAtMid(self,data,pos):
        
        if pos == 1:
            self.insertAtBeg(data)
            return
        
        temp = self.head
        count =  1
        while(count<pos-1):
            temp = temp.next
            count+=1
        
        if temp.next == None:
            self.insertAtLast(data)
            return
        
        
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        
        
    # Deletion at any Position
    def deleteAnyNode(self,pos):
        
        if self.head is None:
            print("List is Empty")
            return
        
        if pos == 1:
            self.head = self.head.next 
            if self.head is None: 
                self.tail = None
                
            return
        
        temp = self.head
        prev = None
        cnt = 1
        while(cnt<pos):
            prev = temp
            temp = temp.next
            cnt +=1
            
            
        prev.next = temp.next
        
        if temp.next is None:
            self.tail = prev
        
    
    def traverse(self):
        current = self.head
        while(current):
            print(current.data, end="->")
            current = current.next
        print("None")
        
    def getLen(self):
        curr = self.head
        len = 0
        while(curr):
            len+=1
            curr = curr.next

        return len 
    
    # Approach 1
    def sortLinkedList(self):
        zeroCount = 0
        oneCount = 0
        twoCount = 0
        
        temp = self.head
        while(temp is not None):
            if temp.data == 0:
                zeroCount+=1
            elif temp.data == 1:
                oneCount+= 1
            elif temp.data == 2:
                twoCount+=1
                
            temp = temp.next
        
        temp = self.head    
        while(temp is not None):
            if zeroCount != 0:
                temp.data = 0
                zeroCount-= 1
            
            elif oneCount != 0:
                temp.data = 1
                oneCount-= 1
                
            elif twoCount != 0:
                temp.data = 2
                twoCount-= 1
                
            temp = temp.next
            
        return self.head
        
    def insertAtTail(self, tail, curr):
        tail.next = curr
        tail = curr
        return tail
    
    def sortLinkedList2(self):
        zeroHead = Node(-1)
        zeroTail = zeroHead # Tail q banay q ki jo v data milega woo tail mai hi jura ga na, toh tail ka jarurat hai 
        oneHead = Node(-1)
        oneTail = oneHead
        twoHead = Node(-1)
        twoTail = twoHead
        
        curr = self.head
        # Seprate list bana diya 0,1,2 ka 
        while curr is not None:
            nextNode = curr.next
            curr.next = None
            value = curr.data
            if value == 0:
                zeroTail = self.insertAtTail(zeroTail, curr)
            elif value == 1:
                oneTail = self.insertAtTail(oneTail, curr)
            elif value == 2:
                twoTail = self.insertAtTail(twoTail, curr)
            
            curr = nextNode
             
        # Next Ab sare ko merge krna hai humko
        
        if oneHead.next is not None:
            zeroTail.next = oneHead.next
        else:
            # One ka list empty hai agar else mai ayi toh toh 2 se jor do
            zeroTail.next = twoHead.next
            
        oneTail.next = twoHead.next
        twoTail.next = None
        
        # Actual head ko sahi position p daldo 
        self.head = zeroHead.next
        
        return self.head

ll = LinkedList()
ll.insertAtLast(2)
ll.insertAtLast(1)
ll.insertAtLast(0)
ll.insertAtLast(1)
ll.insertAtLast(2)

print("Before sorting:")
ll.traverse()

ll.sortLinkedList2()

print("After sorting:")
ll.traverse()


