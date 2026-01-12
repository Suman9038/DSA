# Naive solution :0(n^2)
def getMax(arr: list[int]):
    n = len(arr)
    res = 0
    for i in range(n):
        cur = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] >= arr[i]:
                curr+= arr[i]
            else:
                break
        
        for j in range(i+1, n):
            if arr[j] >= arr[i]:
                curr+= arr[i]
            else:
                break
        res = max(res,curr)
        
    return res

# Effecient SOlution : 0(n),0(n)

def getMaxOptimised(arr: list[int]):
    n = len(arr)
    res = 0
    s = []
    for i in range(n):
        while(s and arr[s[-1]]>= arr[i]):
            tp = s.pop()
            curr = arr[tp] * (i if not s else (i- s[-1]-1))
            res = max(res, curr)
        s.append(i)
    while(s):
        tp = s.pop()
        curr = arr[tp] * (n if not s else (n- s[-1]-1))
        res = max(curr, res)

    return res

arr = [6,2,5,4,1,5,6]
print(getMaxOptimised(arr))