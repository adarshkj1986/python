def symetrical(a):
    n=len(a)
    for i in range(n):
        for j in range(i+1,n):
            if a[i][j]!=a[j][i]:
                return False
    return True
matrix_a=[[1,2,3],
          [2,4,5],
          [3,5,6]]
matrix_b=[[1,2,3],
          [4,5,6],
          [7,8,9]]
print("symmetrical matrix is:",symetrical(matrix_a))
print("unsymmetical matrix is:",symetrical(matrix_b))