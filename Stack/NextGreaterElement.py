# Naive solution: 0(n^2)

def next(arr:list[int]):
    n = len(arr)
    for i in range(n):
        j: int
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                print(arr[j])
                break
        else:
            print(-1)
            
# arr =[15,10,18,12,4,6,2,8]
# prev(arr)

# Effeceint solution :
def nextG(arr:list[int]):
    s = []
    n = len(arr)
    s.append(arr[n-1])
    print(-1)
    for i in range(n-2,-1,-1):
        while(s and s[-1]<= arr[i]):
            s.pop()
        ng = -1 if not s else s[-1]
        print(ng)
        s.append(arr[i])
        
arr =[15,10,18,12,4,6,2,8]
nextG(arr)
