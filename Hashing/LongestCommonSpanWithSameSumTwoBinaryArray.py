#Naive Solution :
def longle(arr1: list[bool],arr2: list[bool]) :
    n= len(arr1)
    res=0
    
    for i in range(0,n) :
        sum1=0
        sum2=0
        for j in range(i,n) :
            sum1+=arr1[i]
            sum2+=arr2[i]
            if(sum1==sum2) :
                res=max(res,j-i+1)
    return res




#Effecient SOlution : 

def lenlong(arr: list[int]) -> int:
    arr = [-1 if x == 0 else 1 for x in arr]
    m = {}
    pre_sum = 0
    max_len = 0

    for i in range(len(arr)):
        pre_sum += arr[i]

        if pre_sum == 0:
            max_len = i + 1
        elif pre_sum in m:
            max_len = max(max_len, i - m[pre_sum])
        else:
            m[pre_sum] = i

    return max_len


def lenBinary(arr1: list[int], arr2: list[int]) -> int:
    n = len(arr1)
    temp = [arr1[i] - arr2[i] for i in range(n)]
    return lenlong(temp)


arr1 = [0,1,0,0,0,0]
arr2 = [1,0,1,0,0,1]
print(lenBinary(arr1, arr2))  

