class Myhash : 
    Bucket: int
    def __init__(self,b: int):
        self.Bucket= b
        self.table = [[] for _ in range(b)]
    def hashFunction(self,key:  int) -> int :
        return key % self.Bucket
    
    def insert(self,key: int) :
        i=self.hashFunction(key)
        if key not in self.table[i] :
            self.table[i].append(key)
    def remove(self, key: int) :
        i= self.hashFunction(key)
        if key in self.table[i] :
            self.table[i].remove(key)
    def search(self, key: int)-> bool :
        i= self.hashFunction(key)
        return key in self.table[i]
    def display(self):
     for i in range(self.Bucket):
        print(f"Bucket {i}: {self.table[i]}")

h= Myhash(7)
h.insert(10)
h.insert(20)
h.insert(15)
h.insert(7)
h.display()
print("Search 15:", h.search(15))  # True
h.remove(15)
print("Search 15 after removal:", h.search(15))