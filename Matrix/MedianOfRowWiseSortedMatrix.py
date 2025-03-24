#Effecient Solution: 0(row*log(maximum element- minimum element)*log cols) :
from bisect import bisect_right

def findMedian(mat: list[list[int]]) -> int:
    row, col = len(mat), len(mat[0])
    
    min_val, max_val = mat[0][0], mat[0][-1]
    
    for i in range(1, row):
        min_val = min(min_val, mat[i][0])   
        max_val = max(max_val, mat[i][-1])  

   
    medpos = (row * col + 1) // 2

   
    while min_val < max_val:
        mid = (min_val + max_val) // 2
        midpos = 0
        for i in range(row):
            midpos += bisect_right(mat[i], mid)

        if midpos < medpos:
            min_val = mid + 1
        else:
            max_val = mid

    return min_val  

matrix = [
    [5,10,20,30,40],
    [1,2,3,4,6],
    [11,13,15,17,19]
]

print("Median is:", findMedian(matrix))
