# #Given a pair-sum array arr[] construct the original array. A pair-sum array for an array is the array that contains sum of all pairs in ordered form, i.e., arr[0] is sum of res[0] and res[1], arr[1] is sum of res[0] and res[2] and so on.

# Note: If the size of original array res[] is n, then the size of pair-sum array arr[] would be n * (n -1) /2. We may assume that the pair-sum array arr[] is appropriate in size.
# Note that, if the original array is correct then the driver code will print true, else false;

class Solution:
    def constructArr(self, arr):
        # code here
        from math import sqrt
        m = len(arr)
        if m == 0:
            return [1]
        if m == 1:
            return [1, arr[0] - 1]

        # Find n from m = n*(n-1)/2
        n = int((1 + sqrt(1 + 8*m)) // 2)
        
         # If n*(n-1)/2 != m → invalid input (avoid index error)
        if n * (n - 1) // 2 != m:
            return []

        res = [0] * n

        # compute res[0]
        res[0] = (arr[0] + arr[1] - arr[n - 1]) // 2

        # compute others
        for i in range(1, n):
            res[i] = arr[i - 1] - res[0]

        return res
arr=[4,5,7]
sol=Solution()
res=sol.constructArr(arr)
print(res)
