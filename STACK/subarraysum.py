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