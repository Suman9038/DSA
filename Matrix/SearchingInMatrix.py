# Naive Solution : 0(R*C): 

def sear(mat:list[list[int]] , x: int) :
    row= len(mat)
    col= len(mat[0])
    for i in range(row) :
        for j in range(col) :
            if(mat[i][j]==x) : 
                print(f"Found at pos ({i},{j})")
                return
    
    print("Not Found")
    
# mat=[
#     [10,20,30,40],
#     [15,25,35,45],
#     [27,29,37,48],
#     [32,33,39,50]
# ]
# sear(mat,x=29)


#Effecient Solution : 0(R+C) :

def searching(mat:list[list[int]] , x: int) :
    row= len(mat)
    col= len(mat[0])
    i= 0
    j= col-1
    while(i<row and j>=0) :
        if(mat[i][j]==x) : 
                print(f"Found at pos ({i},{j})")
                return
        elif (mat[i][j]>x) :
            j-=1
        else :
            i+=1
     
    print("Not Found")
    
mat=[
    [10,20,30,40],
    [15,25,35,45],
    [27,29,37,48],
    [32,33,39,50]
]
searching(mat,x=66)