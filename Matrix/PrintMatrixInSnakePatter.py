def printSnake(matrix: list[list[int]]) :
    row= len(matrix) 
    for i in range(row) :
        if i % 2 ==0 :
            for j in range(len(matrix[i])) :
                print(matrix[i][j],end=" ")
        else :
            for j in range(len(matrix[i])-1,-1,-1) : 
                print(matrix[i][j],end=" ")
                
                
matrix: list[list[int]] =[
    [1,2,3,4,
    5,6,7,8,
    9,10,11,12]
]
printSnake(matrix)