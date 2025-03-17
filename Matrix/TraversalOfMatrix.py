#  Naive Solution :
def Trav(matrix:list[list[int]]) :
    row= len(matrix)
    col = len(matrix[0])
    temp: list[list[int]] =[[0]*row for _ in range(col)] 
    for i in range(row) :
        for j in range(col) :
            temp[i][j]= matrix[j][i]
    
    for i in range(row) :
        for j in range(col) :
          matrix[j][i]=temp[i][j]
    for i in range(row) :
        for j in range(col) :
            print(temp[i][j],end=" ")
        

matrix= [
    [1,2],
    [1,2]
]
# Trav(matrix)

# Effecient Solution :

def Transpose(matrix:list[list[int]]) :
    row= len(matrix)
    col = len(matrix[0])
    for i in range(row) :
        for j in range(i+1,col) :
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            
    for i in range(row) :
        for j in range(col) :
            print(matrix[i][j],end=" ")
            
matrix= [
    [1,2],
    [1,2]
]
Transpose(matrix)