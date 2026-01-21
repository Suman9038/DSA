# #  Using queue.Queue - Efficient and Thread Safe
# from queue import Queue

# q = Queue()

# q.put(1)
# q.put(2)
# q.put(3)

# print("Initial Size of the Queue", q.qsize())
# print("Initial Size of the Queue", q)

# print("Elements dequeued from the queue:")
# print(q.get()) # Ye Element Remove karta hai 
# print("Is empty:", q.empty())
# print(q.get())
# print("Is empty:", q.empty())
# print(q.get())
# print("Is empty:", q.empty())


# q.put(1)
# # print("Is empty:", q.empty())
# print("Is full:", q.full())

# #  Using collections.deque - Efficient
# from collections import deque
# q = deque()

# print("\nUsing collections.deque - Efficient\n")

# q.append('a')
# q.append('b')
# q.append('c')
# print("Initial queue:", q)

# print("Elements dequeued from the queue:")
# print(q.popleft())
# print(q.popleft())
# print(q.popleft())

# print("Queue after removing elements:", q)



from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()
        
    def enqueue(self, data):
        self.q.append(data)
        
    def dequeue(self):
        if self.q.is_empty():
            print("Queue is empty")
        else:
            return self.q.pop()
        
    def peek(self):
        return self.q[0]
    
    def is_empty(self):
        return len(self.q) == 0
    
    def size(self):
        return len(self.q)
    
    def print_queue(self):
        print(self.q)