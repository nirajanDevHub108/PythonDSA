'''
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

 

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation: 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
Example 2:

Input: nums = [21,21]
Output: 64
Example 3:

Input: nums = [1,2,3,4,5]
Output: 0
'''
import math
def sumFourDivisors(nums):
    sumOfDivsior= 0
    for num in nums:
        divisor = set()
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisor.add(i)
                divisor.add(num // i)

            if len(divisor) > 4:
                break
        if len(divisor) == 4:
            sumOfDivsior+=sum(divisor)
    return sumOfDivsior


nums=[1,2,3]
print(sumFourDivisors(nums))