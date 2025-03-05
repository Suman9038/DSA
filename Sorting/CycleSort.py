def cycle(arr: list[int]) : 
    n: int= len(arr)
    for cs in range(0,n-1) :
        item: int= arr[cs]
        pos: int= cs
        for i in range(cs+1, n) :
            if(arr[i]<item) :
                pos+=1
            item , arr[pos] = arr[pos], item
        while(pos!= cs) :
            pos=cs
            for i in range(cs+1, n) :
                if(arr[i]<item) :
                    pos+=1
            item , arr[pos] = arr[pos], item
            
arr: list[int]= [20,40,50,10,30]
cycle(arr)
print(arr)