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

'''
java solution:

class Solution {
    public boolean exist(char[][] mat, String word) {
        int n = mat.length;
        int m = mat[0].length;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (dfs(mat, word, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean dfs(char[][] mat, String word, int i, int j, int idx) {
        if (idx == word.length()) {
            return true;
        }

        if (i < 0 || i >= mat.length || j < 0 || j >= mat[0].length ||
            mat[i][j] != word.charAt(idx)) {
            return false;
        }

        char temp = mat[i][j];
        mat[i][j] = '#'; // mark visited

        boolean found = dfs(mat, word, i+1, j, idx+1) ||
                        dfs(mat, word, i-1, j, idx+1) ||
                        dfs(mat, word, i, j+1, idx+1) ||
                        dfs(mat, word, i, j-1, idx+1);

        mat[i][j] = temp; // backtrack
        return found;
    }
}

'''