matrix=[[2,3,4],
        [5,6,7]]
for j in range(len(matrix[0])):
    col_sum=0
    for i in range(len(matrix)):
        col_sum+=matrix[i][j]
    print("column wise sum is:",col_sum)