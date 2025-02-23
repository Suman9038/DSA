# Naive Solution: 0(n^2) :

def minDifference(arr: list[int]) :
    n: int= len(arr)
    res= float('inf')
    for i in range(1,n) :
        for j in range(i) :
            res=min(res,abs(arr[i]-arr[j]))
    return res
# arr: list[int]= [5,3,8]
# print(minDifference(arr))

# Effecienct solution : time= 0(nlogn) (for sorting) + 0(n) (for traversel of the arrray) = 0(nlogn)

def minDif(arr: list[int]) :
    n: int= len(arr)
    res= float('inf')
    arr.sort()
    print(arr)
    for i in range(1,n) :
        res= min(res,arr[i]-arr[i-1])
    return res

arr: list[int]= [10,8,1,4]
print(minDif(arr))
