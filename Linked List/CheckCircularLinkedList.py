class Node :
    def __init__(self,data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.tail = None
    
    def insertNode(self,element,data):
        
        if self.tail is None:
            new_node = Node(data)
            self.tail = new_node
            new_node.next = new_node
            return

        current = self.tail
        while(current.data != element):
            current = current.next
            # Preventing from the infinite loop if the element is  not found
            if current == self.tail:
                print("Element Not Found")
                return
            
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node
        
        # To updating the tail
        if current == self.tail:
            self.tail = new_node
            
    def deleteNode(self,value):
        # check for the list is empty
        if self.tail is None:
            print("The list is empty nothing to delete")
            return
               
        
        prev = self.tail # cosidering the tail as prev 
        curr = prev.next # prev next  is curr always one step ahead
        
        # if there is only single node in an list
        if prev == curr and curr.data == value:
            self.tail = None
            print(f"Deleted the only node: {value}")
            return
        
        # traverse upto the list to be deleted
        while(curr.data != value):
            prev = curr
            curr = curr.next
            # Stopping it from the infinite loop if the data is not present 
            if curr == self.tail.next :
                print(f"Value {value} not found in the list.")
                return
                    
        # deleting removing the pointer 
        prev.next = curr.next
        
        # if the current node or the node to be dleted is the last node or the tail itself 
        if curr == self.tail:
            self.tail = prev
            
        curr.next = None
        print(f"Deleted node: {value}")
        
    # Function to print the linked list    
    def traverse(self):
        
        if self.tail is None:
            print("List is empty")
            return
        
        temp = self.tail.next
        # print(self.tail.data, end="->")
        while(True):
            print(temp.data, end="->")
            temp = temp.next
            if temp == self.tail.next:
                break
            
        print("(Back to start)")
        
    def checkCircular(self):
        if self.tail is None:
            return True
            
        if self.tail.next is None:
            return False
            
        temp = self.tail.next
        while(temp is not None and temp != self.tail):
            temp = temp.next
        
        if temp is None:
            return False
        else :
            return True
            
            
c = CircularLinkedList()
c.insertNode(5, 10)     
c.insertNode(10, 20)
c.insertNode(20, 30)
c.traverse()
c.insertNode(30, 50)
c.traverse()
c.deleteNode(50)
c.traverse()
print("Is Circular:", c.checkCircular())
            

            
          
            