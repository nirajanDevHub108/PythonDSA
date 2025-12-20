class Solution:
    def searchInsertK(self, arr, k):
        # code here
        for i in range(len(arr)):
            if arr[i]>=k:
                return i
        return len(arr)
k=5
arr=[1,2,3,5,6]
sol=Solution()
res=sol.searchInsertK(arr,k)
print(res)