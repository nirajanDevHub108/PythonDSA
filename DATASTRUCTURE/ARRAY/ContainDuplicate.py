'''
Contains Duplicate
Solved 
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
'''


from typing import List

def hasDuplicate(nums: List[int]) -> bool:
    nums.sort()
    
    if len(nums) == 1:
        return False

    for i in range(1, len(nums)):  # start from index 1 to avoid comparing with nums[-1] accidentally
        if nums[i] == nums[i - 1]:
            return True
    
    return False

# Example calls:
print(hasDuplicate([1, 2, 3, 4]))  # False
print(hasDuplicate([1, 2, 3, 1]))  # True

'''3. Hash Set
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
Time & Space Complexity
Time complexity: 
O(n)
O(n)
Space complexity: 
O(n)
O(n)
'''

# def findDuplicates(self, arr):
#     seen=set()
#     duplicates=set()
#     for num in arr:
#         if num in seen:
#             duplicates.add(num)
#         else:
#             seen.add(num)
#     return list(duplicates)