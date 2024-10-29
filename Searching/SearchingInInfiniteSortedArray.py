def binSearch(arr : list [int] , x : int,low : int , high : int) :
    if(low>high) :
        return -1
    mid : int = int((low + high)/2)
    if(arr[mid] == x) :
        return mid
    elif(x>arr[mid]) :
        return (binSearch(arr,x,mid+1,high))
    else :
        return(binSearch(arr,x,low,mid-1))

# arr : list[int] =[5,10,15,20]
# x : int =15
# n=len(arr)
# low : int =0
# high : int = n-1
# print(binSearch(arr,x,low,high))


# NAIVE SOLUTION : (0(pos))
def SInfinite(arr : list[int] , x : int ) :
    i : int = 0
    while(True) :
        if arr[i] == x :
            return i 
        if arr[i] > x : 
            return -1
        i+=1

arr : list[int] = [1,10,15,20,40,80,100,120,500,600,960,100000]
x : int = 100
# print(SInfinite(arr,x))

# EFFECIENT SOLUTION : (0(log pos))

def Search(arr : list[int] , x : int) :
    if arr[0] == x :
        return 0
    i : int =1
    while(arr[i]<x) :
        i=i*2
    if arr[i] == x :
        return i
    return binSearch(arr,x,i/2+1,i-1)

arr : list[int] =[1,10,15,20,40,60,80,100,200,500,1000]
x : int = 100
print(Search(arr,x))

