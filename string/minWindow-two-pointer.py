'''
You are given two strings, s1 and s2. Your task is to find the smallest substring in s1 such that s2 appears as a subsequence within that substring.

The characters of s2 must appear in the same sequence within the substring of s1.
If there are multiple valid substrings of the same minimum length, return the one that appears first in s1.
If no such substring exists, return an empty string.
Note: Both the strings contain only lowercase english letters.

Examples:

Input: s1 = "geeksforgeeks", s2 = "eksrg"
Output: "eksforg"
Explanation: "eksforg" satisfies all required conditions. s2 is its subsequence and it is smallest and leftmost among all possible valid substrings of s1.
'''
def minWindowSubsequence(s1: str, s2: str) -> str:
    n = len(s1)
    m = len(s2)

    nextPos = [[-1] * 26 for _ in range(n + 1)]

    for c in range(26):
        nextPos[n][c] = -1

    for i in range(n - 1, -1, -1):
        for c in range(26):
            nextPos[i][c] = nextPos[i + 1][c]
        nextPos[i][ord(s1[i]) - ord('a')] = i

    ans = ""
    minLen = float('inf')

    for start in range(n):
        if s1[start] != s2[0]:
            continue

        idx = start + 1  
        ok = True

        # match remaining characters of s2
        for j in range(1, m):
            idx = nextPos[idx][ord(s2[j]) - ord('a')]
            if idx == -1:
                ok = False
                break
            idx += 1

        if ok:
            endIdx = idx - 1
            length = endIdx - start + 1
            if length < minLen:
                minLen = length
                ans = s1[start:start + length]

    return ans

s1 = "geeksforgeeks"
s2 = "eksrg"
print(minWindowSubsequence(s1,s2))