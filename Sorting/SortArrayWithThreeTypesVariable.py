# Naive Solution : time: 0(n) , aux: 0(n)

def sortthree(arr: list[int]) :
    n: int= len(arr) 
    temp: list[int] = [0]*n
    i: int= 0
    for j in range(n) :
        if(arr[j]==0) :
            temp[i]=arr[j]
            i+=1
            
    for j in range(n) :
        if(arr[j]==1) :
            temp[i]=arr[j]
            i+=1
            
    for j in range(n) :
        if(arr[j]==2) :
            temp[i]=arr[j]
            i+=1
    
    for j in range(n) :
        arr[j]=temp[j]
        
arr: list[int]= [0,1,1,2,0,1]
sortthree(arr)
print(arr)

# Effecient solution : time: 0(n)  , aux: 0(1)

def sortThree(arr:list[int]) :
    n: int= len(arr)
    low: int= 0
    mid: int=0
    high: int=n-1
    
    while(mid<=high) :
        if(arr[mid]==0) :
            arr[mid],arr[low]=arr[low],arr[mid]
            mid+=1
            low+=1
        
        elif(arr[mid]==1) :
            mid+=1
            
        else :
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
        
arr: list[int]= [0,1,1,2,0,1]
sortThree(arr)
print(arr)
            