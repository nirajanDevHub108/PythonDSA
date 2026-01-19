class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        rows, cols = len(mat), len(mat[0])

        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                prefix[r][c] = (
                    prefix[r-1][c]
                    + prefix[r][c-1]
                    - prefix[r-1][c-1]
                    + mat[r-1][c-1]
                )

        left, right, ans = 0, min(rows, cols), 0

        while left <= right:
            size = (left + right) // 2
            if self.exists(prefix, size, threshold, rows, cols):
                ans = size
                left = size + 1
            else:
                right = size - 1

        return ans

    def exists(self, prefix, size, limit, rows, cols):
        for r in range(size, rows + 1):
            for c in range(size, cols + 1):
                square_sum = (
                    prefix[r][c]
                    - prefix[r-size][c]
                    - prefix[r][c-size]
                    + prefix[r-size][c-size]
                )
                if square_sum <= limit:
                    return True
        return False
sol=Solution()
mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
threshold = 4
res=sol.maxSideLength(mat,threshold)
print(res)

'''
java code

class Solution {

  int rows, cols;

  // Main function
  public int maxSideLength(int[][] grid, int limit) {

      rows = grid.length;
      cols = grid[0].length;

      // Prefix sum matrix
      int[][] prefix = new int[rows + 1][cols + 1];

      // Build prefix sums
      for (int r = 1; r <= rows; r++) {
          for (int c = 1; c <= cols; c++) {
              prefix[r][c] =
                      prefix[r - 1][c]
                    + prefix[r][c - 1]
                    - prefix[r - 1][c - 1]
                    + grid[r - 1][c - 1];
          }
      }

      int left = 0;
      int right = Math.min(rows, cols);
      int answer = 0;

      // Binary search on square size
      while (left <= right) {
          int size = left + (right - left) / 2;

          if (existsValidSquare(prefix, size, limit)) {
              answer = size;
              left = size + 1;
          } else {
              right = size - 1;
          }
      }

      return answer;
  }

  // Check if any square of given size satisfies threshold
  private boolean existsValidSquare(int[][] prefix, int size, int limit) {

      for (int r = size; r <= rows; r++) {
          for (int c = size; c <= cols; c++) {

              int squareSum =
                      prefix[r][c]
                    - prefix[r - size][c]
                    - prefix[r][c - size]
                    + prefix[r - size][c - size];

              if (squareSum <= limit) {
                  return true;
              }
          }
      }
      return false;
  }
}
'''