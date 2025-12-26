'''        
        itertaive binary search algoritham

        low=0
        high=n-1
        
        while (low <=high):
            mid=low+(high-low)//2 #to avoid overflow
            if (arr[mid] == target):
                return mid
            elif (arr[mid]< target):
                low=mid+1
            else:
                high=mid-1'''
class Solution:
    #it always work on sorted array
    def BinarySearchIterative(self,arr, low, high, target):
        mid=low+(high-low)//2 #to avoid overflow

        if(low > high):
            return -1
        if(arr[mid] == target):
            return mid
            
        elif (arr[mid] < target):
            return self.BinarySearchIterative(arr,mid+1,high,target,)
        else:
            return self.BinarySearchIterative(arr,low,mid-1,target,)
        

        return -1

    
#main code
#n=5
arr = [1,2,3,4,5]
target = 4

sol = Solution()
res = sol.BinarySearchIterative(arr, 0, len(arr) - 1, target)

if res != -1:
    print("Element is present at index", res)
else:
    print("Element is not present in array")

print(res)

'''
it will return the very last occurances even after finding the k it will check for low values 
class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        low=0
        high=len(arr)-1
        res=-1
        while low <=high:
            mid=low+(high-low)//2
            if arr[mid]==k:
                res = mid
                high=mid-1
            elif arr[mid] <k:
                low=mid+1
            else:
                high=mid-1
        return res
'''
