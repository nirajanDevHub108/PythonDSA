# #Given a square matrix mat[][], the task is to swap the elements of the major and minor diagonals.

# Major Diagonal: Elements that lie from the top-left corner to the bottom-right corner of the matrix (i.e., where row index equals column index).
# Minor Diagonal: Elements that lie from the top-right corner to the bottom-left corner (i.e., where the sum of row and column indices equals n - 1).

class Solution:
    def swapDiagonal(self,mat):
        n=len(mat)
        for i in range(n):
            mat[i][i],mat[i][n-1-i] = mat[i][n-1-i],mat[i][i]
        return mat