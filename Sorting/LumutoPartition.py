
def Lpartiton(arr: list[int] , low: int , high: int , pivot :int)->list :
    # pivot: int = arr[high]
    pivot_value = arr[pivot]
    arr[pivot] , arr[high] = arr[high], arr[pivot]
    # print(pivot)
    i: int = low-1
    for j in range(low,high) :
        if(arr[j]<pivot_value) :
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i+1)


arr: list[int] = [10,80,30,90,40,50,70]
# arr: list[int] = [70,60,80,40,30]
n: int = len(arr)
low: int = 0
high: int = n-1
pivot = 4
print(Lpartiton(arr,low,high,pivot))
print(arr)
    