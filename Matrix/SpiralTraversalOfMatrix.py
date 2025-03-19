def spiralTraversal(mat: list[list[int]]) :
    row= len(mat)
    col= len(mat[0]) 
    top=0
    left=0
    right= col-1
    bottom= row-1
    while(top<=bottom and left<=right) :
        for i in range(left , right+1) :
            print(mat[top][i],end=" ")
        top+=1
        for i in range(top , bottom+1) :
            print(mat[i][right],end=" ")
        right-=1
        if(top<=bottom) :
            for i in range(right,left-1,-1) :
                print(mat[bottom][i],end=" ")
            bottom-=1
        if(left<=right) :
            for i in range(bottom,top-1,-1) :
                print(mat[i][left],end=" ")
            left+=1

mat=[
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
]
spiralTraversal(mat)