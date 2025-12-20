'''Given a sorted array arr[] (0-index based) of distinct integers and an integer k, find the index of k if it is present in the arr[]. If not, return the index where k should be inserted to maintain the sorted order.

Examples :

Input: arr[] = [1, 3, 5, 6], k = 5
Output: 2
Explanation: Since 5 is found at index 2 as arr[2] = 5, the output is 2.
here we used linear serach but even after finding k we have to return arr index where that elemnt should present if that k is not there so we just compare the i value arr[i]>=k return i value index value
'''


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