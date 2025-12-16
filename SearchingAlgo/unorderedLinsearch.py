class Solution:
    def unorderedLinearSearch(self,arr,n,target):
        for i in range(n):
            if arr[i]==target:
                return i
        return -1
    
#main code
n=5
arr=[2,4,6,7,8]
target=5
sol=Solution()
res=sol.unorderedLinearSearch(arr,n,target)
print(res)