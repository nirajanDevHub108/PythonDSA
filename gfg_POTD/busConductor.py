'''

'''
class Solution:
    def findMoves(self, chairs, passengers):
        # code here
        chairs.sort()
        passengers.sort()
        sum=0
        for c,p in zip(chairs,passengers):
            sum+=abs(c-p)
            
            
        return sum
sol=Solution()
chairs=[3, 1, 5]
passengers=[2, 7, 4]
res=sol.findMoves(chairs,passengers)
print(res)