class Solution:
    def kthSmallest(self, mat, k):
        n = len(mat)

        # smallest and largest possible values
        low = mat[0][0]
        high = mat[n-1][n-1]

        def count_less_equal(mid):
            """Count elements <= mid in the matrix"""
            count = 0
            row = n - 1
            col = 0

            while row >= 0 and col < n:
                if mat[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count

        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low

mat = [
    [16, 28, 60, 64],
    [22, 41, 63, 91],
    [27, 50, 87, 93],
    [36, 78, 87, 94]
]
k = 3

sol = Solution()
print(sol.kthSmallest(mat, k))  # Output: 27
