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
    
    # Approach 1 Iterative Time: 0(n)
    def reverseLinkedList(self):
        if self.head is None or self.head.next is None :
            print("LinkedList Is Empty")
            return 
        
        prev = None
        curr = self.head
        self.tail = self.head
        
        while curr:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
            
        self.head = prev
        return prev

    # Helper function for recursive approach
    # Approach 2 Recursive Time: O(n)
    def reverse(self,prev,curr):
        
        #  Base case
        if curr is None:
            self.head = prev 
            return prev 
        
        forward = curr.next
        curr.next = prev
        self.reverse(curr,forward)
            
    def reverseLinkedListRecursively(self):
        if self.head is None or self.head.next is None:
            return
        self.tail = self.head
        prev = None
        curr = self.head
        self.reverse(prev,curr)
        
    def reverseKLinkedList(self, head, k):
        if head is None :
            print("List is Empty")
            
            
        prev = None 
        curr = head
        forward = None
        count = 0
        
        while(curr is not None and count < k):
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
            count+=1
            
        # Step 2 Ab ayega recursion se output usko jor do first group k sath
        if forward is not None:
            head.next = self.reverseKLinkedList( forward, k)
         
        # Step 3 Return the previous or the head  
   
        return prev
    
ll = LinkedList()
ll.insertAtBeg(10)
ll.traverse()
ll.insertAtLast(50)
ll.insertAtLast(70)
ll.traverse()
ll.insertAtMid(100,2)
print("Original List:")
ll.traverse()
# ll.deleteAnyNode(3)
print("\nAfter Iterative Reverse:")
ll.reverseLinkedList()
ll.traverse()
print("\nAfter Recursive Reverse:")
ll.reverseLinkedListRecursively()
ll.traverse()
print("\nAfter K-Group Reverse (k=2):")
ll.head = ll.reverseKLinkedList(ll.head, 2)
ll.traverse()

