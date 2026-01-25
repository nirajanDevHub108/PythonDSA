import math

def countValidParentheses(n):
    if n % 2 != 0:
        return 0
    
    k = n // 2
    return math.comb(2 * k, k) // (k + 1)
