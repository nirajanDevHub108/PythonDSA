def countNegatives(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count=0
        for row in grid:
            for val in row:
                if val < 0:
                    count+=1
        return count

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
res=countNegatives(grid)
print(res)