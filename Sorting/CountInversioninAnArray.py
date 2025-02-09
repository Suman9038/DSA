#NAIVE SOLUTION : 0(n^2)

def convInv(arr: list[int]) -> int :
    n: int= len(arr)
    res: int =0
    for i in range(n-1) :
        for j in range(i+1,n) :
            if(arr[i]>arr[j]) :
                res+=1
                
    return res 

# arr: list[int] = [2,4,1,3,5]
# print(convInv(arr))


#EFFECIENT SOLUTION : 0(nlogn) It uses the idea of the merge sort algo just it calculate res for every smaller element

def countandmerge(arr: list[int],low : int ,high : int ,mid: int )-> int :
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
    k: int = low
    res: int = 0
    while(i<n1 and j<n2) :
        if(left[i]<=right[j]) : 
            arr[k]=left[i]
            i+=1
            k+=1
        else :
            arr[k]=right[j]
            j+=1
            k+=1
            res=res+(n1-i)
    while(i<n1) :
        arr[k]=left[i]
        i+=1
        k+=1
    while(j<n2) :
        arr[k]=right[j]
        j+=1
        k+=1
    return res
    
def countInversion(arr: list[int], low: int , high:int) -> int :
    res = 0
    if low < high:
        mid = low + (high - low) // 2
        
        res += countInversion(arr, low, mid)  # Left half
        res += countInversion(arr, mid + 1, high)  # Right half
        res += countandmerge(arr, low, high, mid)  # Count inversions during merge
    
    return res
    
arr: list[int] = [2,5,8,11,3,6,9,13]
print(countInversion(arr,0 ,len(arr) - 1))