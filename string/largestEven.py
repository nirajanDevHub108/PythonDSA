'''
You are given a string s consisting only of the characters '1' and '2'.

You may delete any number of characters from s without changing the order of the remaining characters.

Return the largest possible resultant string that represents an even integer. If there is no such string, return the empty string "".

Example 1:
Input: s = "1112"
Output: "1112"
Explanation:
'''
def largestEven(s):
    if '2' not in s:
        return ""
    for i in range(len(s)-1, -1, -1):
        if int(s[i]) % 2 == 0:
            return s[:i+1]
    '''
    '''

s="1112"
print(largestEven(s))