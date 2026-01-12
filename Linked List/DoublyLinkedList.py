class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Insert at the Begining    
        
    def insertAtHead(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    # Insert at the End
    def insertAtTail(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            
        else :
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
      
    # Insert at any Position      
    def insertAtPos(self,pos,data):
        if pos == 1 :
            self.insertAtHead(data)
            return
        
        temp = self.head
        curr = 1
        while(curr<pos-1):
            temp = temp.next
            curr+=1
            
        if(temp.next == None):
            self.insertAtTail(data)
            return
        
        new_node = Node(data)
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node
        new_node.prev = temp
        
    # Deletion at any Position
    def deleteAnyNode(self,pos):
        if self.head is None:
            print("List is Empty")
            return
        
        if pos == 1:
            temp = self.head
            if temp.next is not None:
                temp.next.prev = None
            self.head = temp.next
            if self.head is None: 
                self.tail = None
            temp.next = None
            return
        
        current = self.head
        previous = None
        count = 1
        while(count<pos):
            previous = current
            current = current.next
            count +=1
            
        
        if current.next is None:
            previous.next = None
            self.tail = previous
            current.prev = None
        else:  # Delete middle node
            previous.next = current.next
            current.next.prev = previous
            current.next = None
            current.prev = None
      
    # Get Length of Linked List                              
    def getLenth(self):
        len = 0
        current = self.head
        while(current):
            len+=1
            current = current.next
        
        return len

    # Traverse the Linked List
    def traverse(self):
        current = self.head
        while(current):
            print(current.data, end= "<->")
            current = current.next
        print("None")

        
dl = DoublyLinkedList()
dl.insertAtTail(10)
dl.insertAtTail(20)
dl.insertAtTail(100)
dl.insertAtTail(500)
dl.insertAtPos(3,200)
dl.insertAtHead(1)
dl.insertAtTail(11010)
print("Length:", dl.getLenth())
dl.traverse()
print("Head:", dl.head.data if dl.head else None)
print("Tail:", dl.tail.data if dl.tail else None)

print("\nDeleting 3rd node (20):")
dl.deleteAnyNode(3)
dl.traverse()

print("\nDeleting 1st node (1):")
dl.deleteAnyNode(1)
dl.traverse()

print("\nDeleting last node (11010):")
dl.deleteAnyNode(dl.getLenth())
dl.traverse()
print("Head:", dl.head.data if dl.head else None)
print("Tail:", dl.tail.data if dl.tail else None)
        
        