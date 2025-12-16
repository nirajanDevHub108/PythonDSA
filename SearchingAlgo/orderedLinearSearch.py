class Solution:
    def orderedLinearSearch(self,arr,n,target):
        for i in range(0,n,2):
            if arr[i]==target:
                return i
            elif arr[i]>target:#at nay point arr[i] value is greater than target we will return -1
                return -1
        return -1
    
#main code
n=5
arr=[2,4,6,7,8]
target=6
sol=Solution()
res=sol.orderedLinearSearch(arr,n,target)
print(res)