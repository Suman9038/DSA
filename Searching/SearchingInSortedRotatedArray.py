
# NAIVE SOLUTION : (0(n)) in worst case scenario

def sear(arr : list[int], x : int )   :
    # without enumerate Function :
    
    # for i in range(len(arr)) : 
    #     if arr[i] == x :
    #      return i
    # return -1
    
    # with enumerate Function :
    
    for i , values in enumerate (arr)  :
        if values == x :
            return i
    return -1
        
arr : list[int] = [100,200,400,1000,10,20]
x : int = 10
# print(sear(arr,x))

# EFFECIENT SOLUTION : (0(log n)) :

def Search(arr : list[int] , x :int ) -> int :
    n= len(arr)
    low : int = 0
    high : int = n-1
    while(low<=high) :
        mid : int = int((low +high)/2)
        if arr[mid] == x :
            return mid 
        if(arr[low]<arr[mid]) : # for left half 
            if x>=arr[low] and x < arr[mid] :  # between left most element and mid does the element exixst or not 
                high = mid -1
            else :
                low = mid +1
        else :  # for right half 
            if x > arr[mid] and x<=arr[high] :  # between right most element and mid element does the element exixst or not 
                low = mid + 1
            else :
                high = mid -1
    return -1

arr : list[int] = [10,20,40,60,5,8]
x : int = 6
print(Search(arr,x))