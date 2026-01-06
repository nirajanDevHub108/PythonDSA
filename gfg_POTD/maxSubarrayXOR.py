'''
Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

Note: A subarray is a contiguous part of any given array.

Examples:

Input: arr[] = [100, 200, 300, 400], k = 2
Output: 700
Explanation: arr2 + arr3 = 700, which is maximum.
'''
def maxSubarrayXOR(arr, k):
        # code here
        n = len(arr)
    
        # XOR of first window
        window_xor = 0
        for i in range(k):
            window_xor ^= arr[i]
    
        max_xor = window_xor
    
        # Slide the window
        for i in range(k, n):
            window_xor ^= arr[i - k]  # remove left element
            window_xor ^= arr[i]      # add right element
            max_xor = max(max_xor, window_xor)
    
        return max_xor

arr = [2, 5, 8, 1, 1, 3]
k = 3
print(maxSubarrayXOR(arr,k))