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

'''
java code:

class Solution {
    public int minimumCost(int[] nums) {
        int n = nums.length;

        // suffixMin[i] = minimum value from nums[i] to nums[n-1]
        int[] suffixMin = new int[n];
        suffixMin[n - 1] = nums[n - 1];

        for (int i = n - 2; i >= 0; i--) {
            suffixMin[i] = Math.min(nums[i], suffixMin[i + 1]);
        }

        int ans = Integer.MAX_VALUE;

        // i is the start index of the 2nd subarray
        for (int i = 1; i < n - 1; i++) {
            int cost = nums[0] + nums[i] + suffixMin[i + 1];
            ans = Math.min(ans, cost);
        }

        return ans;
    }
}

'''