def reverseNumber(n):
    rev_num=0
    while n :
        last_num= n % 10
        rev_num = rev_num * 10 + last_num
        n = n // 10
    return rev_num


n=4569 
print(reverseNumber(n)) #9654