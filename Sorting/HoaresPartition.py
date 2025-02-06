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
        
arr: list[int] =[5,3,8,4,2,7,1,10]
# arr: list[int] =[5,10,9,12]
n: int= len(arr)
low: int = 0
high: int= n-1
print(Hpartition(arr,low,high))
print(arr)

            