

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.q = [None] * size
        self.front = -1
        self.rear = -1
        
    
    def enqueue(self, data):
        # if (self.front == 0 and self.rear == (self.size-1)) or (self.rear == (self.front -1)%(self.size-1)):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return
        
        elif self.front == -1:
            self.front = 0
            self.rear = 0
        
        elif self.rear == self.size-1 and self.front != 0:
            # To maintain cyclic nature
            self.rear = 0
        else:
            self.rear += 1
        
        self.q[self.rear] = data
                    
    def dequeue(self):
        if self.front ==-1:
            print("Queue is empty")
            return
        
        ans = self.q[self.front]
        # self.q[self.front]= -1
        
        if self.front == self.rear: # First Element to pop
            self.front =-1
            self.rear =-1
            
        elif self.front == self.size-1:
            self.front = 0 # To maintain cyclic nature
            
        else:
            self.front +=1
        
        return ans
    
    def print_queue(self):
        if self.front == -1:
            print("Queue is EMPTY")
            return

        i = self.front
        while True:
            print(self.q[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()
        
        
cq = CircularQueue(3)

cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)

cq.print_queue()

print(cq.dequeue())
cq.enqueue(4)

cq.print_queue()