# #Given a square matrix mat[][], the task is to swap the elements of the major and minor diagonals.

# Major Diagonal: Elements that lie from the top-left corner to the bottom-right corner of the matrix (i.e., where row index equals column index).
# Minor Diagonal: Elements that lie from the top-right corner to the bottom-left corner (i.e., where the sum of row and column indices equals n - 1).

class Solution:
    def swapDiagonal(self,mat):
        n=len(mat)
        for i in range(n):
            #here we are swaping each oth index element with the last elemnt ie (n-1-i) and leaving middile row for odd length nxn matrix without affecting their sum
            mat[i][i],mat[i][n-1-i] = mat[i][n-1-i],mat[i][i]
        return mat
    
sol=Solution()
mat =[[0, 1, 2],
      [3, 4, 5],
      [6, 7, 8]]
res=sol.swapDiagonal(mat)
print(res)