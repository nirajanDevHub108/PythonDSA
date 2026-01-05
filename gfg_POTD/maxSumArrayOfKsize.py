'''
Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

Note: A subarray is a contiguous part of any given array.

Examples:

Input: arr[] = [100, 200, 300, 400], k = 2
Output: 700
Explanation: arr2 + arr3 = 700, which is maximum.
'''
nums = [100, 200, 300, 400]
k = 2
def maxOfsubarrayK(arr,k):
    n = len(arr)
    
    if n < k:
        return -1 
    
   
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

print(maxOfsubarrayK(nums,k))