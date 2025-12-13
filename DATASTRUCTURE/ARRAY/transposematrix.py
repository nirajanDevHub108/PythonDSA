class Solution:
    def transpose(self, mat):
        # code here
        x = y = 0
        N = len(mat)
        
        while x < N:
            i, j = x + 1, y + 1
            
            while i < N:
                mat[i][y], mat[x][j] = mat[x][j], mat[i][y]
                i += 1
                j += 1
            
            x += 1
            y += 1
        
        return mat
sol=Solution()
mat = [[1, 1, 1, 1],
       [2, 2, 2, 2],
       [3, 3, 3, 3],
       [4, 4, 4, 4]]
res=sol.transpose(mat)
print(res)