
class Queue:
    def __init__(self):
        self.q = []
        self.front = 0
        self.rear = 0
        # self.size = size Parameter mai ek size lelo and wahi passs krdo
        
    def enqueue(self, data):
        # if fixed size ie given in the queue
        # if self.rear == self.size:
        #     print("Queue is full")
        # else:
        #     self.q[self.rear] = data
        #     self.rear += 1
        
        self.q.append(data)
        self.rear += 1
        
    def dequeue(self):
        if self.front == self.rear:
            print("Queue is empty")
            return None
        else:
            ans = self.q[self.front]
            self.q[self.front] = -1
            self.front +=1
            
            if self.front == self.rear:
                self.front = 0
                self.rear = 0
                
            return ans      
                 
    def front_or_peek(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            return self.q[self.front]
        
    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False
        
        
q = Queue()     # Queue object banaya

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.front_or_peek())   # 10

print(q.dequeue())         # 10
print(q.dequeue())         # 20

print(q.is_empty())        # False

print(q.dequeue())         # 30
print(q.dequeue())         # Queue is empty
        
            