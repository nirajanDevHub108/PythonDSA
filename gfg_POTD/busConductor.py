'''
You are conductor of a bus. You are given two arrays chairs[] and passengers[] of equal length, where chairs[i] is the position of the ith chair and passengers[j] is the position of the jth passenger. You may perform the following move any number of times:

Increase or decrease the position of the ith passenger by 1 (i.e., moving the ith passenger from position x to x+1 or x-1)
Return the minimum number of moves required to move each passenger to get a chair.
Note: Although multiple chairs can occupy the same position, each passenger must be assigned to exactly one unique chair.

T(c)-O(n logn)
space=0(1)
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