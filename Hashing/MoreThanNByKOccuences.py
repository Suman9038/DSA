# Naive solution 0(nlogn)
# def printNByK(arr: list[int], k: int) :
#     n= len(arr)
#     i=1 
#     count= 1
#     arr.sort()
#     while(i<n) :
#         while(i<n and arr[i]==arr[i-1]) :
#             count+=1
#             i+=1
#         if(count>n/k) :
#             print(arr[i-1], end=" ")
#         count=1
#         i+=1

# arr=[10,10,20,30,20,10,10]
# printNByK(arr,k=2)

# Effecient Solution: 0(n)
# def printNbyK(arr:list[int],k:int) :
#     n=len(arr)
#     m={}
    
#     for i in range(0,len(arr)) :
#         m[arr[i]]=m.get(arr[i],0)+1
#         # print(m)
        
#     for key, value in m.items() :
#         if(value>n/k) :
#             print(key)
        
        
        
        
        
# arr=[10,10,20,30,20,10,10]
# printNbyK(arr,k=2)


def printNbyK(arr:list[int],k:int) : 
    n=len(arr) 
    m={}
    
    for i in range(0,n) :
        if(arr[i] in m ) :
            m[arr[i]]+=1
        elif (len(m)<k-1) :
            m[arr[i]]=1
        else :
            keys_to_remove = []
            for key in m:
                m[key] -= 1
                if m[key] == 0:
                    keys_to_remove.append(key)
            for key in keys_to_remove:
                del m[key]
    # Reset counts
    for key in m:
        m[key] = 0 
        
     # Count actual frequencies
    for i in range(0, n):
        if arr[i] in m:
            m[arr[i]] += 1

    for key, value in m.items():
        if value > n // k:
            print(key)

        
arr=[10,10,20,30,20,10,10]
printNbyK(arr,k=2)