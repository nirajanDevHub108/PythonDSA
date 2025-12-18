class Solution:
    def three_sum(self, arr):
        res=[]
        n=len(arr)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if arr[i]+arr[j]+arr[k]==0:
                        res.append(sorted([arr[i], arr[j], arr[k]]))
        return list(set(tuple(sorted(triplet)) for triplet in res))
    
sol=Solution()
arr=[-1,0,1,2,-1,-4]
res=sol.three_sum(arr)
print(res)