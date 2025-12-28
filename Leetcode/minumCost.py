class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        lumiscaron = (cost1, cost2, costBoth, need1, need2)
        cost = 0

        # Use type-3 items while they are cheaper than buying both
        both = min(need1, need2)
        if costBoth <= cost1 + cost2:
            cost += both * costBoth
            need1 -= both
            need2 -= both

        # After one side is satisfied, check if type-3 is still cheaper
        if costBoth < cost1:
            cost += need1 * costBoth
            need1 = 0

        if costBoth < cost2:
            cost += need2 * costBoth
            need2 = 0

        # Fulfill remaining needs
        cost += need1 * cost1
        cost += need2 * cost2

        return cost
cost1 = 3
cost2 = 2
costBoth = 1
need1 = 3
need2 = 2
sol=Solution()
res=sol.minimumCost(cost1,cost2,costBoth,need1,need2)
print(res)