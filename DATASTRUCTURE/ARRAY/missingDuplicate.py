# Given an unsorted array arr[] of size n, containing elements from the range 1 to n, it is known that one number in this range is missing, and another number occurs twice in the array, find both the duplicate number and the missing number.


class Solution:
    
    def findTwoElement(self, arr):
        n= len(arr)
        seen=set()
        duplicates=[]
        for num in arr:
            if num in seen:
                duplicates.append(num)
            else:
                seen.add(num)
        missing=[]
        for i in range(1,n+1):
            if i not in seen:
                missing.append(i)
        return duplicates+missing
sol=Solution()
arr=[1,2,2,4]
res= sol.findTwoElement(arr)
print(res)

