# NAIVE SOLUTION 
def SqrRoot(x : int) :
    i : int =1
    while(i*i<=x) :
        i+=1
    return(i-1)
x : int = 6
# print(SqrRoot(x))

# EFFECIENT SOLUTION 
def sqRoot(x : int ) :
    low : int = 1
    high : int =x
    ans : int =-1
    if(x == 0) :
        return x
    while(low<=high) :
        mid : int = int((low+high)/2)
        msq : int = mid * mid
        if (msq == x) :
            return mid 
        elif (msq > x) :
            high=mid-1
        else : 
            low = mid + 1
            ans = mid
    return ans

a : int =0
print(sqRoot(a))