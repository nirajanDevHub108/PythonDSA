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