def findPeakGrid( mat):
    n = len(mat)
    m = len(mat[0])

    for i in range(n):
        for j in range(m):
            curr = mat[i][j]

            if i > 0 and mat[i-1][j] >= curr:
                continue
            if i < n-1 and mat[i+1][j] >= curr:
                continue
            if j > 0 and mat[i][j-1] >= curr:
                continue
            if j < m-1 and mat[i][j+1] >= curr:
                continue

            return [i, j]  

    return []

mat=[[10, 20, 15],           
    [21, 30, 14],
    [7, 16, 32]]
res=findPeakGrid(mat)
print(res)