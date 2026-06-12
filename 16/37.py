matrix1=[[1,2],
         [3,4]]
result=[[0,0],
        [0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[j][i]=matrix1[i][j]
for matrix in result:
    print(matrix)