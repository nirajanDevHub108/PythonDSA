'''
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

 

Example 1:

Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
op-1
'''
class Solution:
    def numMagicSquaresInside(self, grid):
        row,cols=len(grid),len(grid[0])
        count=0
        def isMagicSqr(i,j):
            square=[
                grid[i][j:j+3],
                grid[i+1][j:j+3],
                grid[i+2][j:j+3]
            ]
            nums = [num for row in square for num in row]
            if set(nums) != set(range(1, 10)):
                return False
            target=sum(square[0])

            for rows in square:
                if sum(rows) != target:
                    return False
            
            #col
            for c in range(3):
                if square[0][c] + square[1][c] + square[2][c] != target:
                    return False

            # diagonals
            if square[0][0] + square[1][1] + square[2][2] != target:
                return False

            if square[0][2] + square[1][1] + square[2][0] != target:
                return False

            return True
        for i in range(row - 2):
            for j in range(cols - 2):
                if isMagicSqr(i, j):
                    count += 1

        return count
grid = [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]

print(Solution().numMagicSquaresInside(grid))
