def minPairSum(nums):
    nums.sort()
    
    left = 0
    right = len(nums) - 1
    max_pair_sum = 0
    
    while left < right:
        pair_sum = nums[left] + nums[right]
        max_pair_sum = max(max_pair_sum, pair_sum)
        left += 1
        right -= 1
    
    return max_pair_sum
nums=[3,4,6,7]
print(minPairSum(nums))
