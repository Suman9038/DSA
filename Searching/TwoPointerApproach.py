# 1.Given an unsdorted array and a number x we need to find the if there is a pair in the arrray with equals to x
#iske liye better approach h hasing woo bad mai karenge 

# naive solution :(0(n2)) :
def fun1(arr : list[int], x : int ) -> bool :
    for i in range(len(arr)) :
        for j in range(len(arr)) :
            if (arr[i] + arr[j] == x) :
                return True
    return False

arr : list[int] = [3,5,9,2,8,10,11]
x : int = 60
# print(fun1(arr,x))

# 2.Given an sdorted array and a number x we need to find the if there is a pair in the arrray with equals to x

def isPair(arr : list[int], left : int , right : int , x : int) -> bool :
    while(left < right ) :
        if (arr[left] + arr[right] == x) :
            return True
        elif (arr[left] + arr[right]>x) :
            right-=1
        else :
            left +=1
    return False 
arr : list[int] = [3,5,9,2,8,10,11]
x : int = 17
n=len(arr)
left : int = 0
right : int = n-1
# print(isPair(arr,left,right,x))

# 3.Given an sdorted array and a number x we need to find the if there is a triplet in the arrray with equals to x

def triplet(arr : list[int] , x : int ) -> bool :
    for i in range(len(arr)) :
        if (isPair(arr,i+1,n-1,x-arr[i])) :
            return True
    return False 

arr : list[int] = [3,5,9,2,8,10,11]
print(triplet(arr,x))