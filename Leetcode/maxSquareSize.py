'''

There is a large (m - 1) x (n - 1) rectangular field with corners at (1, 1) and (m, n) containing some horizontal and vertical fences given in arrays hFences and vFences respectively.

Horizontal fences are from the coordinates (hFences[i], 1) to (hFences[i], n) and vertical fences are from the coordinates (1, vFences[i]) to (m, vFences[i]).

Return the maximum area of a square field that can be formed by removing some fences (possibly none) or -1 if it is impossible to make a square field.

Since the answer may be large, return it modulo 109 + 7.

Note: The field is surrounded by two horizontal fences from the coordinates (1, 1) to (1, n) and (m, 1) to (m, n) and two vertical fences from the coordinates (1, 1) to (m, 1) and (1, n) to (m, n). These fences cannot be removed.

 

Example 1:



Input: m = 4, n = 3, hFences = [2,3], vFences = [2]
Output: 4
Explanation: Removing the horizontal fence at 2 and the vertical fence at 2 will give a square field of area 4.


'''
class Solution:
    def maximizeSquareArea(self, m, n, hFences, vFences):
        MOD = 10**9 + 7

        
        hFences = sorted(hFences + [1, m])
        vFences = sorted(vFences + [1, n])

       
        hGaps = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                hGaps.add(hFences[j] - hFences[i])

        max_side = -1

        
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                gap = vFences[j] - vFences[i]
                if gap in hGaps:
                    max_side = max(max_side, gap)

        if max_side == -1:
            return -1

        return (max_side * max_side) % MOD

    
sol=Solution() 

m = 4
n = 3
hFences = [2,3]
vFences = [2]
print(sol.maximizeSquareArea(m,n,vFences,hFences))

