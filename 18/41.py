matrix=[[2,3,4],
        [5,6,7]]
for i in range(len(matrix)):
    sum_row=0
    for j in range(len(matrix[i])):
        sum_row+=matrix[i][j]
    print("row wise sum is:",sum_row)