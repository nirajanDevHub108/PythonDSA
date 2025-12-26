class Solution:
    def kthMissing(self, arr, k):
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            missing = arr[mid] - (mid + 1)

            if missing < k:
                low = mid + 1
            else:
                high = mid - 1

        return low + k

sol=Solution()
arr = [2,3,4,7,11]
k = 5
res=sol.kthMissing(arr,k)
print(res)