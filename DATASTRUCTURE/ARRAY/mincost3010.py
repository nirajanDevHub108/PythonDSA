def minimumCost(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

    
        suffixMin = [0] * n
        suffixMin[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(nums[i], suffixMin[i + 1])

        ans = float('inf')

        for i in range(1, n - 1):
            cost = nums[0] + nums[i] + suffixMin[i + 1]
            ans = min(ans, cost)

        return ans
nums=[1,2,3,12]
print(minimumCost(nums))