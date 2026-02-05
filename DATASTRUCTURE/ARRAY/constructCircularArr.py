class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        res=[]

        for i in range(n):
            new_indx=(i+nums[i])%n
            res.append(nums[new_indx])
        return res
sol=Solution()
nums = [1, -2, 0, 3]
print(sol.constructTransformedArray(nums))