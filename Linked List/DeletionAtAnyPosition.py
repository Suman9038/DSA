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


ll = LinkedList()
ll.insertAtBeg(10)
ll.traverse()
ll.insertAtLast(50)
ll.insertAtLast(70)
ll.traverse()
ll.insertAtMid(100,2)
ll.traverse()
ll.deleteAnyNode(3)
ll.traverse()


