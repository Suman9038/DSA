# Effecient Solution :0(R*C)
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

def maxRectange(mat: list[list[int]]):
    res = getMaxOptimised(mat[0])
    for i in range(1,len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                mat[i][j]+= mat[i-1][j]
                
        res= max(res, getMaxOptimised(mat[i]))
    
    return res


mat = [
    [1,0,0,1,1],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,1,1,1,1]
]

print(maxRectange(mat))