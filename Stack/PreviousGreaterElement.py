# Naive solution: 0(n^2)

def prev(arr:list[int]):
    n = len(arr)
    for i in range(n):
        j: int
        for j in range(i-1, -1, -1):
            if arr[j] > arr[i]:
                print(arr[j])
                break
        else:
            print(-1)
            
# arr =[15,10,18,12,4,6,2,8]
# prev(arr)

# Effeceint solution :
def prevG(arr:list[int]):
    s = []
    n = len(arr)
    s.append(arr[0])
    print(-1)
    for i in range(1,n):
        while(s and s[-1]<= arr[i]):
            s.pop()
        pg = -1 if not s else s[-1]
        print(pg)
        s.append(arr[i])
        
arr =[15,10,18,12,4,6,2,8]
prevG(arr)
