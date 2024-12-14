def merge(arr: list[int],low : int ,high : int ,mid: int )-> list :
    # length = len(arr)
    n1 : int = mid-low+1
    n2 : int = high-mid
    left: list=[0] * n1
    right: list=[0] * n2
    for x in range(n1) :
        left[x] = arr[low+x] # low diya q ki low ka value change v ho sakta h 
    for x in range(n2) :
        right[x] = arr[mid+1+x]
    i: int = 0
    j: int = 0
    k: int = 0
    while(i<n1 and j<n2) :
        if(left[i]<=right[j]) : 
            arr[k]=left[i]
            i+=1
            k+=1
        else :
            arr[k]=right[j]
            j+=1
            k+=1
    while(i<n1) :
        arr[k]=left[i]
        i+=1
        k+=1
    while(i<n1) :
        arr[k]=right[j]
        j+=1
        k+=1
    for i in range(len(arr)) :
        return arr


arr: list[int]= [10,15,20,40,8,11,55]
low : int = 0
n :int =len(arr)
high =n-1
mid :int =int((low+high)/2)
print(merge(arr,low,high,mid))