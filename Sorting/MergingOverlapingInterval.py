def overlapingMerge(arr: list[list[int]]) :
    n: int= len(arr)
    arr.sort(key=lambda x: x[0])
    res: int= 0
    for i in range(1,n) : 
        if(arr[res][1] > arr[i][0]) :
            arr[res][1]= max(arr[res][1],arr[i][1])
            arr[res][0]= min(arr[res][0],arr[i][0])
        else :
            res+=1
            arr[res] = arr[i]
    for i in range(res+1) :
        print(arr[i][0],arr[i][1])
        
        
arr: list[list[int]] =[[5,10],[3,15],[18,30],[2,7]]
overlapingMerge(arr)       