# SOLUTION WITH 0(nlogn) TIME COMPLEXITY

def minDiff(arr: list[int] , m: int) :
    n: int= len(arr)
    if(m>n) :
        return -1
    arr.sort()
    print(arr)
    res: int= arr[m-1] - arr[0]
    for i in range(n-m+1) :
        res = min(res,(arr[i+m-1] - arr[i]))
    return res

arr: list[int]= [7,3,2,4,9,12,56]
print(minDiff(arr,m=3))