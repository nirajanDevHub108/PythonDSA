'''Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

Note:  A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.'''



def nextPermutation(nums):
    n = len(nums)
    
    # Step 1: Find the pivot
    pivot = 0
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot = i
            break
    
    # Step 2: If no pivot, reverse whole array
    if pivot == -1:
        nums.reverse()
        return nums
    
    # Step 3: Find the smallest number greater than pivot from the right
    for j in range(n - 1, pivot, -1):
        if nums[j] > nums[pivot]:
            nums[pivot], nums[j] = nums[j], nums[pivot]
            break
    
    # Step 4: Reverse the suffix
    nums[pivot + 1:] = reversed(nums[pivot + 1:])
    
    return nums


# Example usage:
arr = [1, 3, 5, 4, 2]
print(nextPermutation(arr))  # Output: [1, 4, 2, 3, 5]
