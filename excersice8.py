matrix=[[1,2],[3,4]]
transpose=[[0,0],[0,0]]
for i in range(len(matrix)):
      for j in range(len(matrix[0])):
          transpose[j][i]=matrix[i][j]
for r in transpose:
    print(r)
