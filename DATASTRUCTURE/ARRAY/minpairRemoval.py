def minimumPairRemoval(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        op=0

        def nonDecreasing(arr):
            for i in range(1,len(arr)):
                if arr[i] < arr[i-1]:
                    return False
            return True
        while not nonDecreasing(nums):
            min_sum=float('inf')
            index=0
            for i in range(len(nums) - 1):
                sum= nums[i]+nums[i+1]
                if sum < min_sum:
                    min_sum = sum
                    index = i
            nums=nums[:index] + [min_sum] + nums[index+2 :]
            op +=1
        return op

nums=[5,2,3,1]

print(minimumPairRemoval(nums))

