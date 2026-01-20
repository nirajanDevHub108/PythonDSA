class Solution:
    def divisors(self, n):
        i=1
        res=[]
        while i <= n:
            if n % i == 0:
                res.append(i)
            i+=1
        return res
n=6
sol=Solution()
print(sol.divisors(n))

'''

'''