def heapify(arr: list[int], n: int,i: int) :
    largest: int= i
    left: int= 2*i+1
    right: int= 2*i+2
    if(left<n and arr[left]>arr[largest]) :
        largest=left
    if(right<n and arr[right]>arr[largest]) :
        largest=right
    if(largest != i) :
        arr[largest] , arr[i] = arr[i] , arr[largest]
        heapify(arr ,n,largest)

def buildHeap(arr: list[int]) :
    n: int= len(arr)
    for i in range(int((n-1)/2) , -1, -1) :
        heapify(arr,n,i)

def sort(arr: list[int]) :
    n: int= len(arr)
    buildHeap(arr)
    for i in range(n-1, 0  , -1) :
        arr[0] , arr[i] = arr[i] , arr[0]
        heapify(arr,i,0)


arr: list[int]= [50,20,10,4,15]
sort(arr)
print(arr)