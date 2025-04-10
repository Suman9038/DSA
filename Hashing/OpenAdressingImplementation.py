class MyHash : 
    def __init__(self,c: int):
        self.capacity=c
        self.size=0
        self.arr= [-1]*self.capacity
    def hashFunc(self,key: int)-> int :
        return key % self.capacity
    def search(self,key: int)-> bool :
        h= self.hashFunc(key)
        i=h
        while(self.arr[i] != -1) :
            if(self.arr[i]== key) :
                return True
            i=(i+1)%self.capacity
            if(i==h) :
                return False
        return False
    def insert(self,key: int)-> bool : 
        if(self.size == self.capacity): 
            return False
        i= self.hashFunc(key)
        while(self.arr[i]!= -1 and self.arr[i]!=-2 and self.arr[i]!= key) :
            i=(i+1)%self.capacity
        if (self.arr[i]==key) :
            return False
        else :
            self.arr[i]=key
            self.size+=1
            return True
    def delete(self,key: int)-> bool :
            h= self.hashFunc(key)
            i=h
            while(self.arr[i] != -1) :
                if(self.arr[i]== key) :
                    self.arr[i]=-2
                    return True
                i=(i+1)%self.capacity
                if(i==h) :
                    return False
    def display(self):
        for i in range(self.capacity):
            print(f"Slot {i}: {self.arr[i]}")
                

# Example Usage
mh = MyHash(7)
mh.insert(49)
mh.insert(56)
mh.insert(72)
print("Before deletion:")
mh.display()

print("Search 56:", mh.search(56))  
mh.delete(56)
print("Search 56 after deletion:", mh.search(56))  

print("After deletion:")
mh.display()

            
             