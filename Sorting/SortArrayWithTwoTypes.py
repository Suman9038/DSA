# NAIVE SOLUTION : 0(n) aux space: 0(n)

def posNeg(arr: list[int]) :
    n: int= len(arr)
    temp: list[int] = [0] *n
    i: int= 0
    for j in range(n) :
        if(arr[j]<0) :
            temp[i]=arr[j]
            i+=1
    for j in range(n) :
        if(arr[j]>=0) :
            temp[i]=arr[j]
            i+=1
    for j in range(n):
        arr[j]=temp[j]
        
# arr: list[int]= [-12,18,-10,15]
# posNeg(arr)
# print(arr)

# EFFECIENT SOLUTION : 0(n) aux space: (1) Idea is the variation of the partition of quicksort we will use the hoare partition
def segPosNeg(arr: list[int]) :
    n: int = len(arr)
    i: int= -1
    j: int= n
    while True :
        while True :
            i+=1
            if(arr[i]>=0) :
                break
        while True :
            j-=1
            if(arr[j]<=0):
                break
        if(i>=j) :
            return
        arr[i],arr[j]=arr[j],arr[i]
        
        
arr: list[int]= [-12,18,-10,15]
segPosNeg(arr)
print(arr)