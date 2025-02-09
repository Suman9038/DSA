# NAIVE SOLUTION : 0(nlogn)

def small(arr: list[int], k: int) :
    n: int= len(arr)
    arr.sort()
    return arr[k-1]

arr: list[int]= [10,5,30,12]
print(small(arr,k=2))

# OPTIMISED SOLUTION : Wrost case:0(n^2) but in average case it can work in liner time by making some assumption

def Lpartiton(arr: list[int] , low: int , high: int )->list :
    pivot: int = arr[high]
    # pivot_value = arr[pivot]
    # arr[pivot] , arr[high] = arr[high], arr[pivot]
    # print(pivot)
    i: int = low-1
    for j in range(low,high) :
        if(arr[j]<pivot) :
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i+1)


def kthSmallest(arr: list[int], k: int) :
    n: int= len(arr)
    low: int= 0
    right: int= n-1
    while(low<=right) :
        p: int= Lpartiton(arr,low,right)
        if(p==k-1) :
            return p
        elif(p > k-1) :
            right= p-1
        else :
            low=p+1
    return -1


arr: list[int]= [10,4,5,8,11,6,260]
print(kthSmallest(arr,k=5))