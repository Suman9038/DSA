#Naive Solution :
def longlen(arr: list[bool]) :
    n= len(arr)
    res=0
    for i in range(0,n) :
        c0=0
        c1=0
        for j in range(i,n) :
            if(arr[j]==0) :
                c0+=1
            else :
                c1+=1
            if(c1==c0) :
                res=max(res,j-i+1)
    return res

# arr: list[bool]=[1,0,1,1,1,0,0]
# print(longlen(arr))

#Effecient Solution :
def lenlong(arr: list[int]) :
    arr = [-1 if x == 0 else 1 for x in arr]
    m = {}
    pre_sum=0
    for i in range(len(arr)):
        pre_sum += arr[i]

        if pre_sum == 0:
            max_len = i + 1
        elif pre_sum in m:
            max_len = max(max_len, i - m[pre_sum])
        else:
            m[pre_sum] = i

    return max_len
arr: list[int]=[1,0,1,1,1,0,0]
print(lenlong(arr))
            