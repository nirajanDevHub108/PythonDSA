class Solution:
    def BinarySearchIterative(self,arr,n,target):
        low=0
        high=n-1
        
        while (low <=high):
            mid=low+(high-low)//2 #to avoid overflow
            if (arr[mid] == target):
                return mid
            elif (arr[mid]< target):
                low=mid+1
            else:
                high=mid-1
        return -1

    
#main code
n=5
arr=[2,4,6,7,8]
target=8
sol=Solution()
res=sol.BinarySearchIterative(arr,n,target)
if res != -1:
    print("Element is present at index", res)
else:
    print("Element is not present in array")
print(res)