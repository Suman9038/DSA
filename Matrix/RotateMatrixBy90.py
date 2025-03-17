# Naive Solution : 0(n^2)time, 0(n^2)Aux :
def rotate(mat:list[list[int]]) :
    row= len(mat)
    col= len(mat[0])
    temp= [[0]*row for _ in range(col)]
    for i in range(row) :
        for j in range(col) :
            temp[j][row-1-i]= mat[i][j]
    for i in range(row) :
        for j in range(col) :
            print(temp[i][j],end=" ")
            
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# rotate(matrix)


#Effecient Solution : 0(n^2)time, 0(1)Aux

def rotate90(mat:list[list[int]]) :
    row= len(mat)
    col= len(mat[0])
    for i in range(row) :
        for j in range(i+1,col) :
             matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(row) :
        low=0
        high=row-1
        while(low<high) :
            mat[low][i],mat[high][i]=mat[high][i],mat[low][i]
            low+=1
            high-=1
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rotate90(matrix)
print(matrix,end="\n")