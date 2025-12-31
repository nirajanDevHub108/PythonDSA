from collections import deque

def latestDayToCross(row, col, cells):
    def can_cross(day):
        # Build grid
        grid = [[0] * col for _ in range(row)]
        for i in range(day):
            r, c = cells[i]
            grid[r-1][c-1] = 1  # mark water

        # BFS from all top row land cells
        q = deque()
        for c in range(col):
            if grid[0][c] == 0:
                q.append((0, c))
                grid[0][c] = 1  # mark visited as water to avoid revisit

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c = q.popleft()
            if r == row - 1:  # reached bottom
                return True
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    q.append((nr, nc))
        return False

    # Binary search on day
    left, right = 1, len(cells)
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if can_cross(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans

# Example
row = 2
col = 2
cells = [[1,1],[2,1],[1,2],[2,2]]
print(latestDayToCross(row, col, cells))  # Output: 2
