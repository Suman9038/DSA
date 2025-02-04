def partiton(arr: list[int] , low: int , high: int , p: int)->list :
    index = 0
    n: int = len(arr)
    temp: list[int] = [0]*(high-low+1)
    for i in range(low,high+1) :
        if(arr[i] <= arr[p]) :
            temp[index] = arr[i]
            index+=1
    for i in range(low ,high+1) :
        if(arr[i]> arr[p]) :
            temp[index] = arr[i]
            index+=1
    for i in range (low,high+1) :
        arr[i] = temp[i-low]
    print(arr)


arr: list[int] = [5,13,6,9,12,11,8]
p: int = 6
low: int = 0
high: int = 6
partiton(arr,low,high,p)