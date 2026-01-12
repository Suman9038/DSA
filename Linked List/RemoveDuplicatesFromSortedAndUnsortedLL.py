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
        
    def traverse(self):
        current = self.head
        while(current):
            print(current.data, end="->")
            current = current.next
        print("None")
        
        
    def removeDuplicateFromSortedLL(self):
        if self.head is None: 
            print("List is Empty")
            return None
            
        curr = self.head
        while(curr is not None):
            if curr.next is not None and curr.data == curr.next.data:
                next_ka_next = curr.next.next
                node_to_delete = curr.next
                curr.next = next_ka_next
            else:
                curr = curr.next
                
        return self.head
        
    def removeDuplicateFromUnSortedLL(self):
        if self.head is None:
            print("Link list is empty")
            
            return None
        visited = {}
        curr = self.head
        prev = None
        
        while(curr is not None):
            if visited.get(curr.data) == True:
                prev.next = curr.next
                if curr ==self.tail:
                    self.tail = prev 
                curr = curr.next
            else:
                visited[curr.data] = True
                prev = curr
                curr = curr.next
            
        return self.head

ll = LinkedList()
print("-------------For sorted--------------")
# ll.insertAtLast(10)
# ll.insertAtLast(10)
# ll.insertAtLast(20)
# ll.insertAtLast(20)
# ll.insertAtLast(20)
# ll.insertAtLast(30)
# print("Before removing duplicates:")
# ll.traverse()
# ll.removeDuplicateFromSortedLL()
# print("After removing duplicates:")
# ll.traverse()

print("-------------For unsorted--------------")
ll.insertAtLast(10)
ll.insertAtLast(20)
ll.insertAtLast(10)
ll.insertAtLast(30)
ll.insertAtLast(20)
print("Before:")
ll.traverse()
ll.removeDuplicateFromUnSortedLL()
print("After:")
ll.traverse()