def isPrime(n):
        #your code goes here
        if n < 2 :
            return False
        
        i = 2
        while i * i <= n:
            # Check if i is a divisor
            if n % i == 0:
                return False
            i += 1

               
        return True
n=5
print(isPrime(n))