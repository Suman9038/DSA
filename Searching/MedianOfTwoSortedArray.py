# NAIVE SOLUTION

#EFFECIENT SOLN :(0(log n1)) :
def getMed(arr1: list[int], arr2 :list[int]) -> float :
    n1 : int = len(arr1)
    n2 : int = len(arr2)
    begin1 : int = 0
    end1 : int = n1
    min1 : int 
    max1 : int 
    min2 : int 
    max2 : int 
    while(begin1<=end1) :
        i1 : int = int((begin1+end1)/2)
        i2 : int = int(((n1+n2+1)/2)-i1)
        if (i1==n1) :  
            min1= float('inf') 
        else : 
            min1=arr1[i1]
            
        
        if (i1==0) :  
            max1= float('-inf') 
        else : 
            max1=arr1[i1-1]
        
        
        if (i2==n2) :  
            min2= float('inf') 
        else : 
            min2=arr2[i2]
        
        
        if (i1==0) :  
            max2= float('-inf') 
        else : 
            max2=arr2[i2-1]
        
        
        if(max2<=min1 and max1<=min2) :
            if(int((n1+n2)%2)==0) :
                return(float((max(max2,max1)+min(min1,min2))/2))
            else :
                return(float(max(max1,max2)))
        elif(max1>min2) :
            end1 = i1-1
        else :
            begin1 = i1+1


arr1 : list[int] = [10,20,30]
arr2 : list[int] = [5,15,25,35,45]
print(getMed(arr1,arr2))