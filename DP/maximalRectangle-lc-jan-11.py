def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Sentinel to clear stack at the end

    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    heights.pop()
    return max_area


def maximalRectangle(matrix):
    
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == '1':
                heights[c] += 1
            else:
                heights[c] = 0

        
        max_area = max(max_area, largestRectangleArea(heights))

    return max_area


# ------------------- Driver Code -------------------

if __name__ == "__main__":
    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]

    print(maximalRectangle(matrix))
