class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ans=[]
        for num in nums:
            if num % 2 == 0:
                ans.append(-1)
            else:
                bit=(num + 1) & -(num + 1)
                ans.append(num - (bit >> 1))
        return ans
nums=[11,13,31]
sol=Solution()
print(sol.minBitwiseArray(nums))