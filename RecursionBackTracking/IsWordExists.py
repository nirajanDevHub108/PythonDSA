class Solution:
    def exist(self, mat, word):
        n, m = len(mat), len(mat[0])

        def dfs(i, j, index):
            # All characters matched
            if index == len(word):
                return True

            # Out of bounds or mismatch
            if i < 0 or i >= n or j < 0 or j >= m or mat[i][j] != word[index]:
                return False

            # Mark visited
            temp = mat[i][j]
            mat[i][j] = '#'

            # Explore all 4 directions
            found = (dfs(i+1, j, index+1) or
                     dfs(i-1, j, index+1) or
                     dfs(i, j+1, index+1) or
                     dfs(i, j-1, index+1))

            # Backtrack
            mat[i][j] = temp
            return found

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True

        return False
sol=Solution()
mat = [['T', 'E', 'E'], ['S', 'G', 'K'], ['T', 'E', 'L']]
word = "GEEK"
print(sol.exist(mat,word))