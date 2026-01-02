def plusOne( digits):
    carry = 1  # we are adding 1
    
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += carry
        if digits[i] < 10:
            return digits
        digits[i] = 0  # digit was 10, carry continues
    
    # if we reach here, all digits were 9
    return [1] + digits

digits=[9]
res=plusOne(digits)
print(res)