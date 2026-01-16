def maxSquareHole(n, m, hBars, vBars):

    def longest_consecutive(arr):
        arr.sort()
        longest = 0
        curr = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1] + 1:
                curr += 1
            else:
                longest = max(longest, curr)
                curr = 1

        return max(longest, curr) if arr else 0

    max_h = longest_consecutive(hBars) + 1
    max_v = longest_consecutive(vBars) + 1

    side = min(max_h, max_v)
    return side * side
n = 2
m = 1
hBars = [2,3]
vBars = [2]
print(maxSquareHole(n, m, hBars, vBars))
