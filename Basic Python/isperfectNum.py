def isPerfect(n):
    i=1
    
    sum=0
    while i < n:
        if i == n:
            break
        if n % i == 0:
            sum += i
        i+=1
    return (sum == n)
n=28
print(isPerfect(n))