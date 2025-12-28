'''Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0'''
def countNegatives(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count=0
        # for row in grid:
        #     for val in row:
        #         if val < 0:
        #             count+=1
        # return count
        n=len(grid)
        m=len(grid[0])
        i,j=0,n-1
        while i <m and j >=0:
                if grid[i][j] <0:
                    count +=m-i
                    j-=1
                else:
                       i+=1
        return count
                    
                    

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
res=countNegatives(grid)
print(res)