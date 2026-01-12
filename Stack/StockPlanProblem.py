# Naive Solution: 0(n^2):

def printSpan(arr: list[int]):
    n= len(arr)
    for i in range(n):
        span = 1
        for j in range(i-1, -1, -1):
            if arr[j]<= arr[i] :
                span+=1
            else:
                break
        print(span)
        
arr = [18,12,13,14,11,16]

printSpan(arr)

# Effecient Solution: 0(n), aux: 0(n)

def printSpanOptimised(arr: list[int]):
    n = len(arr)
    stack =[]
    stack.append(0)
    print(1)
    for i in range(1,n):
        while( stack and arr[stack[-1]]<= arr[i] ):
            stack.pop()
        span = i+1 if not stack else i- stack[-1]
        print(span)
        stack.append(i)
        
arr = [18,12,13,14,11,16]

printSpanOptimised(arr)