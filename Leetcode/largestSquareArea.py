
'''
problem no 3074
There exist n rectangles in a 2D plane with edges parallel to the x and y axis. You are given two 2D integer arrays bottomLeft and topRight where bottomLeft[i] = [a_i, b_i] and topRight[i] = [c_i, d_i] represent the bottom-left and top-right coordinates of the ith rectangle, respectively.

You need to find the maximum area of a square that can fit inside the intersecting region of at least two rectangles. Return 0 if such a square does not exist.


'''
def largestSquareArea(bottomLeft, topRight):
        
        max_Area=0
        n=len(bottomLeft)
        
        for i in range(n):
            for j in range(i+1,n):
                left= max(bottomLeft[i][0],bottomLeft[j][0])
                bottom=max(bottomLeft[i][1],bottomLeft[j][1])
                right=min(topRight[i][0],topRight[j][0])
                top=min(topRight[i][1],topRight[j][1])
                
                if left < right and bottom < top:
                    width=right-left
                    height=top-bottom
                    side=min(width,height)
                    max_Area=max(max_Area,side*side)
        return max_Area

bottomLeft = [[1,1],[2,2],[3,1]]
topRight = [[3,3],[4,4],[6,6]]
print(largestSquareArea(bottomLeft,topRight))