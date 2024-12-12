# NAIVE SOLUTION
def selecsort(arr : list[int]) -> list :
    n : int = len(arr)
    temp : list = [0] * n
    for i in range(n) :
        min_element : int = 0
        for j in range(n) :
            if arr[j]<arr[min_element] :
                 min_element = j
        temp[i] = arr[min_element]
        arr[min_element] = 2**32-1 
    for i in range(n) :
        arr[i] = temp[i]
    return arr

arr : list[int] = [10,5,8,20,2,18]
print (selecsort(arr))


# OPTIMIZED SOLTION OR IN-PLACE IMPLEMENTATION
def selectionsort(arr : list[int]) -> list : 
    n : int = len(arr) 
    for i in range(n) :
        mid_element = i
        for j in range(i + 1, n) :
            if arr[j] < arr[mid_element] :
                mid_element = j 
        temp = arr[mid_element]
        arr[mid_element] = arr[i]
        arr[i] = temp
        # arr[i], arr[mid_element] = arr[mid_element], arr[i] 
    return arr


arr : list[int] = [10,5,8,20,2,18]
print (selectionsort(arr))



# time complexity for theta(n^2)