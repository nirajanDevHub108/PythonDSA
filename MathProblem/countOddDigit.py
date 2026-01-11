def countOddDigit(n):
    count= 0
    
    while n:
        last_digit= n %10
        if last_digit % 2 != 0:
            count += 1
        n = n // 10
    return count
    
    
n=4569
print(countOddDigit(n))