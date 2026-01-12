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
        
    def reverse(self, head):
        curr = head
        prev = None
        nextWala = None
        
        while curr is not None:
            nextWala = curr.next
            curr.next = prev
            prev = curr
            curr = nextWala
            
        return prev
        
    def add(self, first, second):
        carry = 0
        result = LinkedList() # Ek empty linked list bana raha hai jise answer store karenge 
        while(first is not None or second is not None or carry != 0):
            val1 = 0 
            val2 = 0
            if first is not None:
                val1= first.data
            if second is not None:
                val2 = second.data
            # Sum calculate kiya 
            total = carry + val1 + val2
            # last digit nikala 
            digit = total % 10
            # Creating a node and add answer in LL
            result.insertAtLast(digit)
            # Carry nikala
            carry = total//10
            
            if first is not None:
                first = first.next
                
            if second is not None:
                second = second.next 
                
        return result.head
            
            
            
        
    def addTwoLL(self, first, second):
        # Step 1 First reverse both of LL
        first = self.reverse(first)
        second = self.reverse(second)
        
        # Step 2 ab add kr dete hai dono ko 
        ansHead = self.add(first, second)
        
        # Step 3 ab mujhe reverse kardena hai answer ko 
        
        ansHead = self.reverse(ansHead)
        
        return ansHead
        

ll1 = LinkedList()
ll1.insertAtLast(4)
ll1.insertAtLast(5)

ll1.traverse()

ll2 = LinkedList()
ll2.insertAtLast(3)
ll2.insertAtLast(4)
ll2.insertAtLast(5)

ll2.traverse()

resultList = LinkedList()
resultList.head = resultList.addTwoLL(ll1.head, ll2.head)

print("Result:")
resultList.traverse()





 