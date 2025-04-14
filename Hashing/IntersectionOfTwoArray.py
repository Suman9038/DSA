# Naive Solurion : 0(m*(m+n)) :
def inter(a: list[int],b:list[int]) :
    m: int= len(a)
    n: int= len(b)
    res=0
    for i in range(0,m) :
        flag: bool= False
        for j in range(0,i) :
            if (a[j] == a[i]) :
                flag= True
                break
        if(flag == True) :
            continue
        for j in range(0,n) :
            if(a[i]==b[j]) :
                res+=1
                break
    return res
# a: list[int]=[10,15,20,15,30,30,5]
# b: list[int]=[30,5,30,80]
# print(inter(a,b))

# Effecient Solution : 0(m+n) , aux= 0(m)
def intersection(a: list[int],b:list[int]) :
    s=set()
    m: int= len(a)
    n: int= len(b)
    res=0
    for i in range(0,m) :
        s.add(a[i]) 
    for j in range(0,n) :
        if b[j] in s :
            res+=1
            s.remove(b[j]) 
    return res

a: list[int]=[10,15,20,15,30,30,5]
b: list[int]=[30,5,30,80]
print(intersection(a,b))