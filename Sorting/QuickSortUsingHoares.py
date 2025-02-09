def Hpartition(arr: list[int], low: int, high: int) :
    pivot: int= arr[low] 
    i: int= low-1
    j: int= high+1
    while (True) :
        while(True) :
            i+=1
            if arr[i] >= pivot :
                break
        while(True) :
            j-=1
            if arr[j] <= pivot:
                break
        if(i>=j) :
            return j
        arr[i],arr[j] = arr[j], arr[i]

def qSort(arr: list[int] , low:int , high: int) :
    if(low<high) :
        p: int= Hpartition(arr,low,high)
        qSort(arr,low,p)
        qSort(arr,p+1,high)
        
arr: list[int]= [8,4,7,9,3,10,5]
low: int= 0
high: int= len(arr)-1
qSort(arr,low,high)
print(arr)