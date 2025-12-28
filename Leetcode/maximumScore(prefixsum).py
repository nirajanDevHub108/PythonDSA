class Solution(object):
    def maximumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        suffxmin=[0]*n
        suffxmin[-1]=nums[-1]

        for i in range(n-2,-1,-1):
            suffxmin[i]=min(nums[i],suffxmin[i+1])

        prefxsum=0
        maxscore=float('-inf')

        for i in range(n-1):
            prefxsum+=nums[i]
            score=prefxsum-suffxmin[i+1]
            maxscore= max(maxscore,score)
        return maxscore

nums = [10,-1,3,-4,-5]

sol=Solution()
res=sol.maximumScore(nums)
print(res)  