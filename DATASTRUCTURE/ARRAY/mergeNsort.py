class Solution:
    def mergeNsort(self, arr1, arr2):
        # code here
        res=list(set(arr1 + arr2))
        res.sort()
        return res

arr1=[5,7,9]
arr2=[4,3,7,1]

sol = Solution()
result= sol.mergeNsort(arr1,arr2)
print(result)