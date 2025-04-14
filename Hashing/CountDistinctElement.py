# Naive Approach : 0(n^2) :
def countDis(arr : list[int]) :
    n: int= len(arr) 
    res: int= 0
    for i in range(0,n) :
        flag: bool= False
        for j in range(0,i) :
            if(arr[i]== arr[j]) :
                flag= True
                break
        if flag== False :
            res+=1
    return res

# arr: list[int]=[10,20,10,20,10,30]
# print(countDis(arr))

# Effecient Solution : 0(n), auxspace: 0(n) :
def countDisctinct(arr: list[int]) :
    n:int= len(arr)
    s=set()
    for i in range(0,n) :
        s.add(arr[i])
    return len(s)

arr: list[int]=[10,20,10,20,10,30]
print(countDisctinct(arr))