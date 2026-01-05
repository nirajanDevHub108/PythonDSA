nums = [100, 200, 300, 400]
k = 2
def maxOfsubarrayK(arr,k):
    n = len(arr)
    
    if n < k:
        return -1  # Edge case
    
    # Sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

print(maxOfsubarrayK(nums,k))