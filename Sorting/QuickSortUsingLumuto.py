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


def qSort(arr: list[int] , low:int , high: int) :
    if(low<high) :
        p: int= Lpartiton(arr,low,high)
        qSort(arr,low,p-1)
        qSort(arr,p+1,high)

arr: list[int]= [8,4,7,9,3,10,5]
low: int= 0
high: int= len(arr)-1
qSort(arr,low,high)
print(arr)
        