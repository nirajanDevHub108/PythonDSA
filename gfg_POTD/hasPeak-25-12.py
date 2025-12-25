'''
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

    return [] T(c)=O(n*m)
optimal will be in O(nlog m)
using binary search
'''
def findPeakGrid( mat):
    n=len(mat)#row
    m=len(mat[0]) #column 

    low=0
    high=m-1
    while low <=high:
        mid=(low+high)//2

        #finiding max element in mid col

        max_row=0
        for i in range(n):
            if mat[i][mid] > mat[max_row][mid]:
                max_row=i
        mid_val=mat[max_row][mid]
        left=mat[max_row][mid-1] if mid-1 >=0 else float("-inf")
        right=mat[max_row][mid+1] if mid+1 < m else float("-inf")

        if mid_val >= left and mid_val>=right:
            return [max_row,mid]
        elif right >mid_val:
            low=mid+1
        else:
            high=mid-1
    return []




mat=[[46,46]]

res=findPeakGrid(mat)
print(res)