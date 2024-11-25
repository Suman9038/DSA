# Naive Recursive SOlution
def sum(arr: list[int], b: int, e: int) -> int:
    s = 0
    for i in range(b, e):
        s += arr[i]
    return s

def minimumPage(arr: list[int], n: int, k: int) -> int:
    if k == 1:
        return sum(arr, 0, n)
    if n == 1:
        return arr[0]
    
    res = (2 ** 31) - 1  # Initialize result with a large value
   
    for i in range(1, n):  # Iterate through all possible split points
        left_max = minimumPage(arr, i , k - 1)  # Left part: first i elements
        right_sum = sum(arr, i, n)  # Right part: elements from i to n-1
        
        res = min(res, max(left_max, right_sum))
    
    return res

# arr = [10, 20, 30, 40]
# n = len(arr)
# k = 2
# print(minimumPage(arr, n, k)) 


# Binary Approach 

def isFeasible(arr : list[int], n: int, k: int, ans: int ) -> bool : 
    req : int = 1
    sum : int = 0 
    for i in range (n) :
        if (sum + arr[i] > ans) :
            req+=1
            sum =arr[i]
        else :
            sum +=arr[i]
        
    return req <= k

def minPage(arr : list[int], n: int , k: int) -> int :
    sum : int = 0
    mx : int = 0
    for i in range(n) :
        sum +=arr[i]
        mx=max(mx,arr[i]) 
    low : int = mx
    high : int = sum 
    res : int = 0
    while (low <= high) :
        mid : int = int((low+high)/2)
        if(isFeasible(arr,n,k,mid)) :
            res = mid       # if Feasible it will go to left part
            high =mid -1 
        else :
            low =mid +1     # else it will go to the right
             
    return res   
    
    

arr = [10, 20, 30, 40]
n = len(arr)
k = 2
print(minPage(arr, n, k)) 