class Solution(object):
    def minAllOneMultiple(self, k):
        """
        :type k: int
        :rtype: int
        """
        onedigit=1*k
        rem=0
        seen=set()
        for len in range(1,k+1):
            rem = (rem * 10 + 1) % k

            if rem %k ==0:
               return len
            if rem in seen:
                return -1

            seen.add(rem)

        return -1
            
sol = Solution()
print(sol.minAllOneMultiple(3))  # Output: 3
       