def bubblesort(arr : list[int]) -> list : 
    n : int = len(arr)
    for i in range(n-1) :
        swapped : bool = False
        for j in range(n-i-1) :
            if arr[j] > arr[j+1] : 
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped =True
                
        if not swapped:
            break
    return arr

# NAIVE SOLUTION : 0((m+n)*log(m+n))

def union(a : list[int] , b: list[int]) :
    n: int= len(a)
    m: int= len(b)
    c: list[int] =[0]*(n+m)
    for i in range(n) :
        c[i] = a[i]
    for i in range(m) :
        c[n+i] = b[i]
    
    bubblesort(c)
    
    for i in range(m+n) :
        if(i==0 or c[i]!=c[i-1]) :
            print(c[i])
            
# a: list[int]=[10,20,20]
# b: list[int]=[5,20,40,40]
# union(a,b)


#EFFECEINT SOLUTION : 0(m+n) idhar v same humlog merge function of merge sort ka idea use karenge

def printUnion(a : list[int] , b: list[int]) :
    n: int= len(a)
    m: int= len(b)
    i: int =0  
    j: int =0
    while(i<n and j<m) :
        if(i>0 and a[i]==a[i-1]) :
            i=i+1
            continue
        if(j>0 and b[j]==b[j-1]) :
            j=j+1
            continue
        if(a[i]<b[j]) :
            print(a[i])
            i+=1
        elif(a[i]>b[j]) :
            print(b[i])
            j+=1
        else :
            print(a[i])
            i+=1
            j+=1
    while(i<n) :
            if(i>0 and a[i]!=a[i-1]) :
                print(a[i])
                i=i+1
    while(j<m) :
            if(j>0 and b[j]!=b[j-1]) :
                print(b[j])
                j+=1


a: list[int]=[10,20,20]
b: list[int]=[5,20,40,40]
printUnion(a,b)