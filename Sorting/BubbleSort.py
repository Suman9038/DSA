def bubblesort(arr : list[int]) -> list : 
    n : int = len(arr)
    for i in range(n-1) :
        swapped : bool = False
        for j in range(n-i-1) :
            if arr[j] > arr[j+1] : 
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped =True
                
        if not swapped:
            break
    return arr

arr : list[int] =[6,8,6,6]
print(bubblesort(arr))