# Naive Solution : 0((m+n)*(m+n)) , aux space= 0(m+n)
def unionFind(a: list[int],b:list[int]) :
    m: int= len(a)
    n: int= len(b)
    c= [0]*(m+n)
    for i in range(0,m) :
        c[i] = a[i]
    for i in range(0,n) :
        c[m+i]=b[i]
    res=0
    for i in range(0,len(c)) :
        flag= False
        for j in range(0,i) :
            if(c[i]==c[j]) :
                flag= True
                break
        if(flag==False) :
            res+=1
    return res

# a: list[int]=[15,20,5,15]
# b: list[int]=[15,15,15,20,10]
# print(unionFind(a,b))

# Effecient Solution : 0(m+n), aux space= 0(m+n)
def unionCount(a: list[int],b:list[int]) :
    m: int= len(a)
    n: int= len(b)
    s= set()
    for i in range(0,m) :
        s.add(a[i])
    for j in range(0,n) :
        s.add(b[j])
    return len(s)


a: list[int]=[15,20,5,15]
b: list[int]=[15,15,15,20,10]
print(unionCount(a,b))
