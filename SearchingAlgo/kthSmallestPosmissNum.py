'''
Given a sorted array of distinct positive integers arr[], You need to find the kth positive number that is missing from the arr[].

Examples:

Input: arr[] = [2, 3, 4, 7, 11], k = 5
Output: 9
Explanation: Missing are 1, 5, 6, 8, 9, 10… and 5th missing number is 9.
'''

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