# Problem: Given a 2D integer array mat[][] and a number x, 
# find whether element x is present in the matrix or not.

class Solution:
    
    def searchMatrix(self, matrix, x):
        num_rows = len(matrix)
        if num_rows == 0:
            return False

        num_columns = len(matrix[0])

        for r in range(num_rows):
            for c in range(num_columns):
                if matrix[r][c] == x:
                    return True
        
        return False


# ----------------------------
# Test Example
# ----------------------------
mat = [
    [6, 23, 21],
    [4, 45, 32],
    [69, 11, 87]
]

x = 32

sol = Solution()
result = sol.searchMatrix(mat, x)
print(result)   # Expected Output: True
