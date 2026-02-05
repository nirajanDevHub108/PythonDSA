class Solution:
    def maxOnes(self, arr, k):
        start = 0
        zeros = 0
        res = 0

        for end in range(len(arr)):
            if arr[end] == 0:
                zeros += 1

            while zeros > k:
                if arr[start] == 0:
                    zeros -= 1
                start += 1

            res = max(res, end - start + 1)

        return res
sol=Solution()
arr = [1, 0, 1]
k = 1
print(sol.maxOnes(arr,k))