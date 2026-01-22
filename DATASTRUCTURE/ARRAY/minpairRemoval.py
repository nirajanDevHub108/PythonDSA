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

'''
java code

import java.util.*;

class Solution {

    public int minimumOperations(int[] nums) {
        List<Integer> list = new ArrayList<>();
        for (int n : nums) list.add(n);

        int ops = 0;

        while (!isNonDecreasing(list)) {
            int minSum = Integer.MAX_VALUE;
            int idx = 0;

            // find leftmost adjacent pair with minimum sum
            for (int i = 0; i < list.size() - 1; i++) {
                int sum = list.get(i) + list.get(i + 1);
                if (sum < minSum) {
                    minSum = sum;
                    idx = i;
                }
            }

            // replace the pair
            list.set(idx, minSum);
            list.remove(idx + 1);
            ops++;
        }

        return ops;
    }

    private boolean isNonDecreasing(List<Integer> list) {
        for (int i = 1; i < list.size(); i++) {
            if (list.get(i) < list.get(i - 1)) {
                return false;
            }
        }
        return true;
    }

    // Optional main for testing
    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {5, 2, 3, 1};
        System.out.println(s.minimumOperations(nums)); // Output: 2
    }
}

'''