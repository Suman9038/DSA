#Naive Solution

def mergeArray(a: list[int] , b: list[int])-> list :
    m: int= len(a)
    n: int= len(b)
    c : list = [0] * (m+n)
    for i in range(m) :
        c[i] = a[i]
    for i in range(n) :
        c[m+i] =b[i]
    c.sort()
    return c

# a : list[int] =[10,15,20,20]
# b : list[int] =[1,12]
# print(mergeArray(a,b))


#Effeciennt Solution :
def mergetwoarray(a: list[int] , b: list[int])-> list :
    m: int= len(a)
    n: int= len(b)
    i : int= 0
    j : int= 0
    while(i<m and j<n) :
        if(a[i]<=b[j]) :
            print(a[i])
            i=i+1
        else :
            print(b[j])
            j=j+1
    while(i<m) :
        print(a[i])
        i=i+1
    while(j<n) :
        print(b[j])
        j=j+1
    
a : list[int] =[10,15,20,20]
b : list[int] =[1,12]
print(mergeArray(a,b))
            