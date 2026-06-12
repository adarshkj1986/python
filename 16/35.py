matrix1=[[1,2,3],
         [4,5,6]]
matrix2=[[8,2,3],
         [2,4,6]]
result=[[0,0,0],
        [0,0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j]=matrix1[i][j]+matrix2[i][j]
for matrix in result:
    print(matrix)