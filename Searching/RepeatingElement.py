#Super Naive Soln : 0(n^2) time and 0(1) space

def superNaive(arr : list[int]) -> int :
    j : int 
    for i in range(len(arr)) :
        for j in range(i+1,len(arr)) :
             if arr[i] == arr[j] :
                return arr[i]

# arr : list[int] = [0,1,2,3,2,2]
# print(superNaive(arr))


def Naive(arr : list[int]) -> int :
    arr.sort()
    n =len(arr)
    for i in range(n) :
        if arr[i] == arr[i+1] :
            return arr[i]

# arr : list[int] = [0,1,2,3,2,2]
# print(Naive(arr))

def EffecientSoln(arr : list[int]) -> int :
    n=len(arr)
    visited : list[bool] =[False] * n
    for i in range(n) :
        if(visited[arr[i]]) :
            return arr[i]
        visited[arr[i]] = True
        

arr : list[int] = [0,1,2,3,2,2]
print(EffecientSoln(arr))


#Repeating Element 0(n) time , 0(1) space and no change in originl array
#but some modifictaion is done in the input array

def findRep(arr : list[int]) -> int :
    slow : int = arr[0]
    fast : int = arr[0]
    while True :
        slow = arr[slow]
        fast = arr[arr[fast]] 
        if slow == fast :
            break
    slow =arr[0]
    while (slow != fast) :
        slow = arr[slow]
        fast = arr[fast]
    return slow

arr : list[int] = [1,2,3,2,2,2]
print(EffecientSoln(arr))


#Solution for input array having element from 0

def findRep(arr : list[int]) -> int :
    slow : int = arr[0]+1
    fast : int = arr[0]+1
    while True :
        slow = arr[slow]+1
        fast = arr[arr[fast]] +1
        if slow == fast :
            break
    slow =arr[0]
    while (slow != fast) :
        slow = arr[slow]+1
        fast = arr[fast]+1
    return slow-1

arr : list[int] = [0,2,1,3,5,4,6,3]
print(EffecientSoln(arr))