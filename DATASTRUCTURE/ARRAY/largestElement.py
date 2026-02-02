def largestElement(nums):
        max = nums[0]
        for i in range(len(nums)):
            if nums[i] > max:
                max = nums[i]
        return max
nums=[4,5,3,7,1,9]
print(largestElement(nums))