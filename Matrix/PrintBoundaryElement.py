def bTraversal(matrix: list[list[int]]) :
    row= len(matrix) 
    cols = len(matrix[0])
    if row == 1: 
        for i in range(cols) :
            print(matrix[0][i],end=" ")
    elif(cols==1) :
        for i in range(row) :
            print(matrix[i][0],end=" ")
    else :
        for i in range(cols) :
            print(matrix[0][i],end=" ")
        for i in range(1,row) :
            print(matrix[i][cols-1],end=" ")
        for i in range(cols-2,-1,-1) :
            print(matrix[row-1][i],end=" ")
        for i in range(row-2,0,-1) :
            print(matrix[i][0],end=" ")

matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
]
bTraversal(matrix)