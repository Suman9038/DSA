# Naive solution : 0(n^2)time 

def isSubArraySum(arr:list[int],sum: int) :
    n= len(arr)
    for i in range(0,n) :
        curr_sum=0
        for j in range(i,n) :
            curr_sum+=arr[j]
            if(curr_sum==sum) :
                return True
    return False

# Effecient Solution : 0(n)time and 0(n) aux space
def isSumSubarray(arr:list[int],sum:int) :
    n= len(arr)
    s=set()
    pre_sum=0
    for i in range(0,n) :
        pre_sum+=arr[i]
        if(pre_sum-sum in s) :
            return True
        if(pre_sum==sum) :
            return True
        s.add(pre_sum)
    return False

arr:list[int]=[3,2,5,6,10]
sum=10
print(isSumSubarray(arr,sum))