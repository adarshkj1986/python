matrix=[[2,3,4],
        [4,5,6]]
result=[[0,0],
        [0,0],
        [0,0]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        result[j][i]=matrix[i][j]
for matrix in result:
    print(matrix)