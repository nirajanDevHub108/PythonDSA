def minRemovals(nums, k):
    nums.sort()
    n = len(nums)

    left = 0
    max_len = 0

    for right in range(n):
        # shrink window until it becomes valid
        while nums[right] > k * nums[left]:
            left += 1

        # update maximum valid window size
        max_len = max(max_len, right - left + 1)

    return n - max_len
nums = [1, 3, 6, 2]
k = 2
print(minRemovals(nums,k))