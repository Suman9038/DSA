def buckSort(arr: list[int], k: int) :
    n: int= len(arr)
    max_val: int= arr[0]
    for i in range(1,n) :
        max_val=max(arr[i],max_val)
    max_val+=1
    
    bkt: list[list[int]]= [[] for _ in range(k)]
    for i in range(n) :
        bi: int= int(k*(arr[i]/max_val))
        bkt[bi].append(arr[i])
    for i in range(k) :
        bkt[i].sort()    
    
    index: int=0
    for i in range(k) :
        for j in bkt[i] :
            arr[index] = j
            index+=1
arr: list[int]=[30,40,10,80,5,12,70]
buckSort(arr,4) 
print(arr)