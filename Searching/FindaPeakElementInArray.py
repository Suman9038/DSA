#  NAIVE SOLUTION : (0(n)) :

def peak(arr : list[int]) -> int :
    n=len(arr) 
    if n==1 :
        return arr[0]
    if arr[0] > arr[1] : 
        return arr[0] 
    if arr[n-1] > arr[n-2] : 
        return arr[n-1] 
    for i in range(n) :
        if arr[i]> arr[i-1] and arr[i] > arr[i+1] :
            return arr[i]

arr : list[int] = [5,10,20,15,7] 
# print(peak(arr)) 

#  EFFECIENT SOLUTION : (0(log n)) :

def PeakElement( arr : list[int] ) -> int :
    n = len(arr) 
    low : int = 0
    high : int =n-1
    while(low <= high) :
        mid : int = int((low +high)/2)
        if (mid ==0 or arr[mid]> arr[mid -1]) and (mid == n-1 or arr[mid]> arr[mid+1]) :
            return arr[mid] 
        if mid > 0 and arr[mid-1]>=arr[mid] :
            high= mid -1
        else :
            low = mid +1 
    return -1

arr : list[int] = [5,20,40,30,20,50,60]
print(PeakElement(arr))
         
                         
        