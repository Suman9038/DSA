def countSort(arr: list[int], k: int):
    n: int = len(arr)
    count: list[int] = [0] * k  

    for i in range(n):  
        count[arr[i]] += 1
    
    
    for i in range(1, k):  
        count[i] += count[i - 1]

    
    output: list[int] = [0] * n
    for i in range(n - 1, -1, -1):  
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1 
   
    for i in range(n):
        arr[i] = output[i]

arr: list[int] = [5, 6, 5, 2]
countSort(arr, 7)
print(arr)  
