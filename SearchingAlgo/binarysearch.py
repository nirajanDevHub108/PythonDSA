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
arr = [2, 4, 6, 7, 8]
target = 8

sol = Solution()
res = sol.BinarySearchIterative(arr, 0, len(arr) - 1, target)

if res != -1:
    print("Element is present at index", res)
else:
    print("Element is not present in array")

print(res)
