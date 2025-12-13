# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

class Solution():
    def suffle(self,arr,n):
        res=[]
        for i in range(n):
            res.append(arr[i])
            res.append(arr[i+n])
        return res
sol=Solution()
arr=[2,5,1,3,4,7]
n = 3
result=sol.suffle(arr,n)
print(result)

