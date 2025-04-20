# Naive solution : 0(n^2)time 

def isSubArray(arr:list[int]) :
    n= len(arr)
    for i in range(0,n) :
        curr_sum=0
        for j in range(i+1,n) :
            curr_sum+=arr[j]
            if(curr_sum==0) :
                return True
    return False

# arr:list[int]=[4,-3,2,1]
# print(isSubArray(arr))


# Effecient Solution : 0(n)time and 0(n) aux space
def is0Subarray(arr:list[int]) :
    n= len(arr)
    s=set()
    pre_sum=0
    for i in range(0,n) :
        pre_sum+=arr[i]
        if(pre_sum in s) :
            return True
        if(pre_sum==0) :
            return True
        s.add(pre_sum)
    return False

arr:list[int]=[4,-3,2,1]
print(isSubArray(arr))
