# NAIVE SOLUTION : 0(nxm)

def intersect(a : list[int] , b: list[int]) :
    n: int= len(a)
    m: int= len(b)
    for i in range(n) :
        if(i>0 and a[i]==a[i-1]) :
            continue
        for j in range(m) :
            if(a[i]==b[j]) :
                print(a[i])
                break

# a: list[int]=[1,20,20,40,60]
# b: list[int]=[2,20,20,20]
# # intersect(a,b)


# EFFECIENT SOLUTION : 0(n+m) using idea of the merge function

def intersection(a : list[int] , b: list[int]) :
    n: int= len(a)
    m: int= len(b)
    i: int =0  
    j: int =0
    while(i<n and j<m) :
        if(i>0 and a[i]==a[i-1]) :
            i=i+1
            continue
        if(a[i]<b[j]) :
            i+=1
        elif(a[i]>b[j]) :
            j+=1
        else :
            print(a[i])
            i+=1
            j+=1


a: list[int]=[1,20,20,40,60]
b: list[int]=[2,20,20,20]
intersection(a,b)    