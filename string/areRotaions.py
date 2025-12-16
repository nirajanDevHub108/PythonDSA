class Solution:
    def areRotations(self, s1, s2):
        # code here
        if len(s1) != len(s2):
            return False
        temp=s1+s1
        
        return s2 in temp
sol=Solution()
s1="abcd"
s2="cdaa"
res=sol.areRotations(s1,s2)
print(res)