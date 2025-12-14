class Solution:
    def prefixSum2D(self, mat, queries):
        # code here 
        n=len(mat) #row length
        m=len(mat[0]) #column length

        #declare prefix sum matrix 
        prefixSum=[[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                prefixSum[i][j]=mat[i][j]

                if i > 0:
                    prefixSum[i][j] += prefixSum[i-1][j]
                if j > 0:
                    prefixSum[i][j] +=prefixSum[i][j-1]
                if i > 0 and j >0:
                    prefixSum[i][j] -= prefixSum[i-1][j-1]
        #result arr
        result=[]
        for r1,c1,r2,c2 in queries:
            total=prefixSum[r2][c2]

            if r1 > 0:
                total -= prefixSum[r1-1][r2]
            if c1 >0:
                total -= prefixSum[r2][c1-1]
            if r1>0 and c1>0:
                total+=prefixSum[r1-1][c1-1]
            
            result.append(total)

        return result







mat= [[1, 2, 3], 
     [1, 1, 0],
     [4, 2, 2]]

queries = [[0, 0, 1, 1], [1, 0, 2, 2]]
sol=Solution()

res=sol.prefixSum2D(mat,queries)

print(res)