'''You are given a sorted array arr[] and a 2D array queries[][], where queries[i] represents a query in the form [l, r, x]. For each query, count how many times the number x appears in the subarray arr[l...r] (inclusive).

Examples:

Input: arr[] = [1, 2, 2, 4, 5, 5, 5, 8], queries[][] = [[0, 7, 5], [1, 2, 2], [0, 3, 7]]
Output: [3, 2, 0]
Explanation:
Query [0, 7, 5] → elements from index 0 to 7 are [1, 2, 2, 4, 5, 5, 5, 8].
Number 5 occurs 3 times.
Query [1, 2, 2] → subarray is [2, 2], and 2 occurs 2 times.
Query [0, 3, 7] → subarray is [1, 2, 2, 4], and 7 is not present.

we have used binary search tree to get the first and last occurances and then compre to get the x occurances in particular sub array of l-r range
'''


class Solution:
    def countX(self, arr, queries):
        result = []

        for l, r, x in queries:
            first = self.first_occurrence(arr, x)
            if first == -1:
                result.append(0)
                continue

            last = self.last_occurrence(arr, x)

            start = max(first, l)
            end = min(last, r)

            if start > end:
                result.append(0)
            else:
                result.append(end - start + 1)

        return result

    def first_occurrence(self, arr, x):
        low, high = 0, len(arr) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                ans = mid
                high = mid - 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def last_occurrence(self, arr, x):
        low, high = 0, len(arr) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                ans = mid
                low = mid + 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return ans


# 🔹 DRIVER CODE
if __name__ == "__main__":
    arr = [1, 2, 2, 4, 5, 5, 5, 8]
    queries = [[0, 7, 5], [1, 2, 2], [0, 3, 7]]

    sol = Solution()
    output = sol.countX(arr, queries)

    print(output)