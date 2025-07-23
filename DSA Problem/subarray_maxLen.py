def maxlen(arr, n, k):
    # Initialize pointers and variables
    left, right, sum, max_len = 0, 0, 0, 0
    
    # Iterate through the array using the right pointer
    while right < n:
        # Add the current element to the sum
        sum += arr[right]
        
        # Shrink the window from the left if the sum exceeds k
        while sum > k:
            sum = sum - arr[left]  # Subtract the leftmost element from the sum
            left += 1  # Move the left pointer to the right
        
        # Update the maximum length if the current sum is within the limit
        if sum <= k:
            max_len = max(max_len, right - left + 1)
        
        # Move the right pointer to the next element
        right += 1
    
    # Return the maximum length of the subarray
    return max_len

# Example input
n = 5
arr = [1, 2, 3, 4, 5]
k = 5

# Call the function and print the result
res = maxlen(arr, n, k)
print(res)  # Output: 2         