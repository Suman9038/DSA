#Naive Solution : 0(n^2) , 0(1) :
def countF(arr: list[int]) :
    n: int= len(arr) 
    for i in range(0,n) :
        flag: bool= False
        for j in range(0,i) :
            if (arr[i] == arr[j]) :
                flag= True
                break
        if(flag == True) :
            continue
        freq= 1
        for j in range(i+1,n) :
            if(arr[i]==arr[j]) :
                freq+=1
        print(f"{arr[i]}  {freq}")

# arr: list[int]=[10,20,20,30,10]
# countF(arr)


#Effecient Solution : 0(n) , aux=0(n) :
def countFreq(arr: list[int]) :
    m={}
    for i in arr :
        m[i]=m.get(i,0)+1
    for key,values in m.items() :
        print(f"{key}  {values}")
        

arr: list[int]=[10,20,20,30,10]
countFreq(arr)    