def countSort(arr: list[int], exp: int):
    n: int = len(arr)
    count: list[int] = [0] * 10 

    for i in range(n):  
        count[(arr[i]//exp)%10] += 1
    
    
    for i in range(1, 10):  
        count[i] += count[i - 1]

    
    output: list[int] = [0] * n
    for i in range(n - 1, -1, -1):  
        output[count[(arr[i]//exp)%10] - 1] = arr[i]
        count[(arr[i]//exp)%10] -= 1 
   
    for i in range(n):
        arr[i] = output[i]
        
def radSort(arr: list[int]) :
    n: int= len(arr)
    mx: int= arr[0]
    for i in range(1,n) :
        if arr[i] > mx :
            mx= arr[i]
    exp: int= 1
    while mx//exp > 0 :
        countSort(arr,exp)
        exp*=10


arr: list[int]= [319,216,6,8,100,50]
radSort(arr)
print(arr)
