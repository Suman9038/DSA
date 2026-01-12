class MinStack :
    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, x: int):
        if not self.stack:
            self.stack.append(x)
            self.minStack.append(x)
        else :
            self.stack.append(x)
            
            if self.minStack[-1] >= self.stack[-1]:
                self.minStack.append(x)
    
    def pop(self):
        if not self.stack:
            return None
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        
        self.stack.pop()
    
    def getMin(self):
        if not self.minStack:
            return None
        return self.minStack[-1]
        
s = MinStack()
s.push(5)   # stack=[5], minStack=[5]
s.push(3)   # stack=[5,3], minStack=[5,3]
s.push(7)   # stack=[5,3,7], minStack=[5,3]
s.push(2)   # stack=[5,3,7,2], minStack=[5,3,2]

print(s.getMin())  # 2
s.pop()            # pops 2 → minStack=[5,3]
print(s.getMin())
        
        
        
# Effecient Solution : Time: 0(1), Aux:0(1)

class Stack :
    def __init__(self):
        self.stack =[]
        self.mini= None
    
    def push(self, x: int):
        if not self.stack:
            self.stack.append(x)
            self.mini = x
        else:
            if x < self.mini:
                val = 2*x - self.mini
                self.stack.append(val)
                self.mini = x
            else:
                self.stack.append(x)
    
    def pop(self):
        if not self.stack:
            return None
        curr = self.stack.pop()
        if curr >= self.mini:
            return curr
        else:
            prevMini = self.mini
            self.mini = 2*self.mini - curr
            return prevMini
    
    def getMini(self):
        if not self.stack:
            return None
        return self.mini
    
s = Stack()
s.push(5)  
s.push(3)   
s.push(7)   
s.push(2)  

print(s.getMini())  
s.pop()            
print(s.getMini()) 
s.pop()           
print(s.getMini())  
s.pop()           
print(s.getMini()) 