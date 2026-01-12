class KStack:
    def __init__(self,k1,n):
        self.K = k1
        self.size = n
        self.arr = [None]*n
        self.top = [-1]*k1
        self.next = [None]*n
        
        self.freeTop = 0
        
        for i in range(n):
            self.next[i]= i+1
        self.next[n-1] = -1
        
    def push(self,x,sn):
        i = self.freeTop
        self.freeTop = self.next[sn]
        self.next[i] = self.top[sn]
        self.top[sn] = i
        self.arr[i] = x
    
    def pop(self, sn):
        i = self.top[sn]
        self.top[sn] = self.next[i]
        self.next[i] = self.freeTop
        self.freeTop = i
        return self.arr[i]
    
ks = KStack(3, 10)  # 3 stacks, array size 10

ks.push(15, 0)
ks.push(45, 0)

ks.push(17, 1)
ks.push(49, 1)

ks.push(39, 2)

print(ks.pop(0))  # 45
print(ks.pop(1))  # 49
print(ks.pop(2))  # 39
    
    
