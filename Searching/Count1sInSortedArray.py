def CountOnes (arr : list[int] , n : int) :
    low : int =0
    high : int = n-1
    while(low<=high) :
        mid : int =int((low+high)/2)
        if(arr[mid] == 0) :
            low =mid+1
        else :
            if(mid==0 or arr[mid-1] != arr[mid]) :
                return (n-mid)
            else :
                high =mid - 1

arr : list[int] =  [0,0,1,1,1,1,1]
n : int = len(arr)
print(CountOnes(arr,n))