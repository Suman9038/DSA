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
    
    def solve(self,first,second):
        
        # If only one element is present in first list uska next1 toh None hoga toh usko directly merge with the second
        if first.next is None:
            first.next = second
            return first
        
        # For first LL
        curr1 = first
        next1 = curr1.next
        # For second LL
        curr2 = second
        next2 = curr2.next
        
        while(next1 is not None and curr2 is not None):
            if curr2.data >= curr1.data and curr2.data <= next1.data:
                # If true hai condittion Ye add krna hai first list
                curr1.next = curr2
                next2 = curr2.next
                curr2.next = next1
                
                # updating the pointer
                curr1 = curr2
                curr2 = next2
            else:
                curr1= next1
                next1 = next1.next
                
                if next1 == None:
                    curr1.next = curr2
                    return first
                    
        return first
                    
    
    def mergeTwoSortedLL(self, first, second):
        
        # Agar first LL empty hai toh ye return kardo
        if first == None:
            return second
        # Agar second LL empty hai toh ye first return kardo
        if second == None:
            return first
        # checking konsa bara hai konsa chota first ll ka first element ya second ka    
        if first.data <= second.data:
            return self.solve(first,second)
        else:
            return  self.solve(second,first)
            
            
        
        

ll1 = LinkedList()
ll1.insertAtLast(1)
ll1.insertAtLast(3)
ll1.insertAtLast(5)

ll1.traverse()

ll2 = LinkedList()
ll2.insertAtLast(2)
ll2.insertAtLast(4)
ll2.insertAtLast(6)

ll2.traverse()

mergedHead = ll1.mergeTwoSortedLL(ll1.head, ll2.head)

temp = mergedHead
# Traversing the merge linked list
while temp:
    print(temp.data, end="->")
    temp = temp.next
print("None")



 