"""
Given a positive integer `n`, repeatedly add all its digits to create a new number.
Continue this process until the resultant number has only one digit.
Return the final single-digit number obtained after performing the operation.

Parameters:
n (int): A positive integer.

Returns:
int: The single-digit number obtained after repeatedly summing the digits of `n`.
"""
#n = 1234 o/p = 1
def totalsum (num):
    while num >= 10:
        total =0
        while num > 0:
            last_digit = num % 10 
            total += last_digit
            num = num // 10
        num = total
    return total

'''def digitSum(n):
    while n // 10 != 0:
        n = totalsum(n)
    return n'''

n =1234

res = totalsum(n)
print(res)