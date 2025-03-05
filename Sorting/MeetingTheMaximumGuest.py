def maxGuest(arr: list[int], dep: list[int]) :
    n: int= len(arr)
    arr.sort()
    dep.sort()
    i:int =1
    j:int =0
    res:int =1
    current:int =1
    while(i<n and j<n) :
        if(arr[i] <= dep[j]) :
            i+=1
            current+=1
        else :
            j+=1
            current-=1
        res = max(res,current)
    return res


arr: list[int]= [900,600,700]
dep: list[int]= [1000,800,700]
print(maxGuest(arr,dep))
