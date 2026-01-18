class Solution:
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])

        row = [[0] * (C + 1) for _ in range(R)]
        col = [[0] * C for _ in range(R + 1)]

        for i in range(R):
            for j in range(C):
                row[i][j + 1] = row[i][j] + grid[i][j]

        for j in range(C):
            for i in range(R):
                col[i + 1][j] = col[i][j] + grid[i][j]

        ans = 1

        for i in range(R):
            for j in range(C):
                for size in range(min(R - i, C - j), ans, -1):
                    if self.isMagic(grid, row, col, i, j, size):
                        ans = size
                        break
        return ans
    
    def isMagic(self,g,r,c,x,y,l):
        target=r[x][y+l] - r[x][y]

        for i in range(l):
            if r[x + i][y + l] - r[x + i][y] != target:
                return False

        for j in range(l):
            if c[x + l][y + j] - c[x][y + j] != target:
                return False

        d1 = d2 = 0
        for k in range(l):
            d1 += g[x + k][y + k]
            d2 += g[x + l - 1 - k][y + k]

        return d1 == target and d2 == target
    
grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]

sol=Solution()
print(sol.largestMagicSquare(grid))

'''
java code
class Solution {
    public int largestMagicSquare(int[][] mat) {
        int R = mat.length;
        int C = mat[0].length;

        // Row prefix sum
        int[][] rowSum = new int[R][C];
        for (int r = 0; r < R; r++) {
            rowSum[r][0] = mat[r][0];
            for (int c = 1; c < C; c++) {
                rowSum[r][c] = rowSum[r][c - 1] + mat[r][c];
            }
        }

        // Column prefix sum
        int[][] colSum = new int[R][C];
        for (int c = 0; c < C; c++) {
            colSum[0][c] = mat[0][c];
            for (int r = 1; r < R; r++) {
                colSum[r][c] = colSum[r - 1][c] + mat[r][c];
            }
        }

        int maxSize = 1;

        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {

                // ✅ FIX HERE
                int maxPossible = Math.min(R - r, C - c);

                for (int size = maxPossible; size > maxSize; size--) {
                    if (isMagic(r, c, size, mat, rowSum, colSum)) {
                        maxSize = size;
                        break;
                    }
                }
            }
        }
        return maxSize;
    }

    private boolean isMagic(
            int sr, int sc, int size,
            int[][] mat, int[][] rowSum, int[][] colSum) {

        int target = rowSum[sr][sc + size - 1]
                   - (sc > 0 ? rowSum[sr][sc - 1] : 0);

        // Check rows
        for (int r = sr; r < sr + size; r++) {
            int sum = rowSum[r][sc + size - 1]
                    - (sc > 0 ? rowSum[r][sc - 1] : 0);
            if (sum != target) return false;
        }

        // Check columns
        for (int c = sc; c < sc + size; c++) {
            int sum = colSum[sr + size - 1][c]
                    - (sr > 0 ? colSum[sr - 1][c] : 0);
            if (sum != target) return false;
        }

        // Main diagonal
        int d1 = 0;
        for (int k = 0; k < size; k++)
            d1 += mat[sr + k][sc + k];
        if (d1 != target) return false;

        // Anti-diagonal
        int d2 = 0;
        for (int k = 0; k < size; k++)
            d2 += mat[sr + size - 1 - k][sc + k];

        return d2 == target;
    }
}

'''