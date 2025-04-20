# Naive Solution : 0(n^2) :
def pair(arr: list[int], sum:int)-> bool :
    n=len(arr) 
    for i in range(0,n) :
        for j in range(i+1,n) :
            if(arr[i]+arr[j]==sum) :
                return True
    return False

# arr: list[int]=[5,8,-2,6]
# sum=3
# print(pair(arr,sum))

# Effecient solution : 0(n) time , 0(n) aux space

def isPair(arr: list[int], sum:int)-> bool :
    n=len(arr) 
    s=set()
    for i in range(0,n) : 
        c= sum - arr[i]
        if(c in s) :
            return True
        s.add(arr[i])
    return False
arr: list[int]=[5,8,-2,6]
sum=3
print(isPair(arr,sum))