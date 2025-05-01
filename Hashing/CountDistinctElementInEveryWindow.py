# Naive Solution 
def counDisc(arr: list[int],k:int) :
    n=len(arr)
    for i in range(0,n-k+1) :
        count=0
        for j in range(0,k) :
            flag= False
            for p in range(0,j) :
                if(arr[i+j]==arr[i+p]) :
                    flag=True
                    break
            if(flag==False) :
                count+=1
        print(count)

# arr=[10,10,5,3,20,5]
# counDisc(arr,4)


#Effecient Solution :0(n) :
def distinctCount(arr: list[int], k: int):
    n = len(arr)
    m = {}

    # First window
    for i in range(k):
        m[arr[i]] = m.get(arr[i], 0) + 1
    print(len(m))  # Distinct count for the first window

    # Slide the window
    for i in range(k, n):
        # Remove frequency of the outgoing element
        m[arr[i - k]] -= 1
        if m[arr[i - k]] == 0:
            del m[arr[i - k]]

        # Add frequency of the incoming element
        m[arr[i]] = m.get(arr[i], 0) + 1

        # Print the count of distinct elements
        print(len(m))

   
arr=[10,10,5,3,20,5]
distinctCount(arr,4)
    