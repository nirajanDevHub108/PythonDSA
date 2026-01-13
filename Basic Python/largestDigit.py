'''
You are given an integer n. Return the largest digit present in the number.
Example 1
Input: n = 25
Output: 5
Explanation: The largest digit in 25 is 5.
Example 2
Input: n = 99
Output: 9
Explanation: The largest digit in 99 is 9.
'''

def largestDigit(n):
    largest_value = 0
    while n > 0:
        last_digit = n % 10
        if largest_value < last_digit:
            largest_value = last_digit
        n = n // 10
    return largest_value
            
n=25
print(largestDigit(n))

