class Solution:
    def subArrayRanges(self, nums):
        n = len(nums)

        def get_sum(is_min):
            stack = []
            left = [0] * n
            right = [0] * n

            
            for i in range(n):
                count = 1
                while stack and (
                    nums[stack[-1][0]] > nums[i] if is_min else nums[stack[-1][0]] < nums[i]
                ):
                    count += stack.pop()[1]
                left[i] = count
                stack.append((i, count))

            stack.clear()

            
            for i in range(n - 1, -1, -1):
                count = 1
                while stack and (
                    nums[stack[-1][0]] >= nums[i] if is_min else nums[stack[-1][0]] <= nums[i]
                ):
                    count += stack.pop()[1]
                right[i] = count
                stack.append((i, count))

            total = 0
            for i in range(n):
                total += nums[i] * left[i] * right[i]

            return total

        return get_sum(False) - get_sum(True)
sol=Solution()
nums=[1,2,3]
print(sol.subArrayRanges(nums))


'''
java class

import java.util.*;

public class SubarrayRangeSum {

    public static void main(String[] args) {
        int[] arr = {1, 2, 3};

        int result = subArrayRanges(arr);
        System.out.println("Sum of subarray ranges: " + result);
    }

    public static int subArrayRanges(int[] nums) {
        long maxSum = getSum(nums, false); // sum of subarray maximums
        long minSum = getSum(nums, true);  // sum of subarray minimums
        return (int) (maxSum - minSum);
    }

    private static long getSum(int[] nums, boolean isMin) {
        int n = nums.length;
        Stack<int[]> stack = new Stack<>();
        int[] left = new int[n];
        int[] right = new int[n];

        // Count elements on the left
        for (int i = 0; i < n; i++) {
            int count = 1;
            while (!stack.isEmpty() &&
                  (isMin ? stack.peek()[0] > nums[i]
                         : stack.peek()[0] < nums[i])) {
                count += stack.pop()[1];
            }
            left[i] = count;
            stack.push(new int[]{nums[i], count});
        }

        stack.clear();

        // Count elements on the right
        for (int i = n - 1; i >= 0; i--) {
            int count = 1;
            while (!stack.isEmpty() &&
                  (isMin ? stack.peek()[0] >= nums[i]
                         : stack.peek()[0] <= nums[i])) {
                count += stack.pop()[1];
            }
            right[i] = count;
            stack.push(new int[]{nums[i], count});
        }

        long sum = 0;
        for (int i = 0; i < n; i++) {
            sum += (long) nums[i] * left[i] * right[i];
        }

        return sum;
    }
}


'''