'''
Given a sorted array of nums and an integer x, write a program to find the lower bound of x.



The lower bound algorithm finds the first and smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.



If no such index is found, return the size of the array.


Example 1

Input : nums= [1,2,2,3], x = 2

Output:1

Explanation:

Index 1 is the smallest index such that arr[1] >= x.
'''
def lowerBound(nums, x):
    n=len(nums)
    low=0
    high=n-1
    ans=len(nums)
    while low <= high:
        mid = (low + high) //2 # over flow control
            
        if nums[mid] >= x :
            ans=mid
            high=mid-1
        elif x > nums[mid]:
            low=mid+1
        else:
            high =mid-1
    return ans
nums=[1,2,2,3]
x= 2
res=lowerBound(nums,x)
print(res)