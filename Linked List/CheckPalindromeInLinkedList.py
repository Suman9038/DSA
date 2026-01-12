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
    
    # Approach 1:
    # def checkPalindrome(self, arr):
    #     n = len(arr)
    #     s = 0
    #     e = n-1
    #     while(s<=e):
    #         if arr[s] != arr[e]:
    #             return False
    #         s+=1
    #         e-=1
            
    #     return True
        
    # def isPalindrome(self):
    #     arr = []
    #     temp = self.head
    #     while temp is not None:
    #         arr.append(temp.data)
    #         temp = temp.next 
            
    #     return self.checkPalindrome(arr)
    
    # Approach 2:
    def getMid(self):
        if self.head is None: 
            return None
        slow = self.head
        fast = self.head.next
        
        while fast is not None and fast.next is not None :
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
        
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
    
    
    def isPalindrome(self):
        if self.head is None or self.head.next is None:
            return True
        
        # step 1
        mid = self.getMid()
        
        # Step 2 : Reverse krna hai middle k age wala node
        temp = mid.next
        mid.next = self.reverse(temp)
        
        # Step 3 : compare both half
        
        head1 = self.head
        head2= mid.next
        
        while head2 is not None:
            if head1.data != head2.data:
                return False
                
            head1 = head1.next
            head2 = head2.next
            
        # Step 4 : repeat step 2 Jise orginal LL mil jaye 
        mid.next = self.reverse(mid.next)
        
        return True

        
ll = LinkedList()
ll.insertAtLast(1)
ll.insertAtLast(2)
ll.insertAtLast(1)
ll.traverse()
print(ll.isPalindrome())
