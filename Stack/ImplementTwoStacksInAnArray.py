class TwoStack:
    def __init__(self,n):
        self.size = n
        self.arr = [None]*n
        self.top1 = -1
        self.top2 = n-1
        
    def push1(self,x):
        if self.top1 < self.top2-1:
            self.top1 += 1
            self.arr[self.top1] = x
        else:
            print("Stack Overflow - Stack1")
            
    def push2(self,x):
        if self.top1+1 < self.top2:
            self.top2 -= 1
            self.arr[self.top2] = x
        else:
            print("Stack Overflow - Stack2")
            
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            print("Stack Underflow - Stack1")
            return None
        
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            print("Stack Underflow - Stack1")
            return None

stacks = TwoStack(10)

stacks.push1(1)
stacks.push1(2)
stacks.push2(9)
stacks.push2(8)

print(stacks.pop1())  # 2
print(stacks.pop2())  # 8
print(stacks.pop1())  # 1
print(stacks.pop2())  # 9