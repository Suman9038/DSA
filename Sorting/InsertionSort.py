def insertionsort(arr :list[int]) -> list :
    n : int = len(arr)
    for i in range(1,n) :
        key : int = arr[i]
        j=  i-1
        while(j>=0 and arr[j]>key) :
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

arr : list[int] =[20,5,40,60,10,30]
print(insertionsort(arr))