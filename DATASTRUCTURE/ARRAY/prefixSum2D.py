class Solution:
    def prefixSum2D(self, mat, queries):
        # code here 
        n=len(mat) #row length
        m=len(mat[0]) #column length

        #declare prefix sum matrix 
        prefixSum=[[0]*m for _ in range(n)]
        






mat= [[1, 2, 3], 
     [1, 1, 0],
     [4, 2, 2]]

queries = [[0, 0, 1, 1], [1, 0, 2, 2]]
sol=Solution()

res=sol.prefixSum2D(mat,queries)

print(res)