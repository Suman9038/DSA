# Naive Solution : 0(nlogn) :
def Longest(arr: list[int] ) :
    n=len(arr) 
    res=1
    curr=1
    arr.sort()
    for i in range(1,n) :
        if(arr[i]==arr[i-1]+1) :
            curr+=1
        else :
            res=max(res,curr)
            curr=1
    res= max(res,curr) 
    return res

# arr=[1,9,3,4,2,20]
# print(Longest(arr))


#Effecient Solution : 0(n) :
def LongestLengh(arr: list[int] ) :
    n=len(arr)
    res=0
    s=set()
    for i in range(0,n):
        s.add(arr[i])
    for i in range(0,n) :
        if(arr[i]-1 not in s) :
            curr=1
            while(arr[i]+curr in s) :
                curr+=1
            res=max(res,curr)
    return res

arr=[1,9,3,4,2,20]
print(LongestLengh(arr))   