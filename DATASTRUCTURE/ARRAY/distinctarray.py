'''You are given two arrays a[] and b[], return the Union of both the arrays in any order.

The Union of two arrays is a collection of all distinct elements present in either of the arrays. If an element appears more than once in one or both arrays, it should be included only once in the result.

Note: Elements of a[] and b[] are not necessarily distinct.
Note that, You can return the Union in any order but the driver code will print the result in sorted order only.'''
def distinctarr(a , b):
    nums = a + b
    n = len(nums)
    nums.sort()
    result=[]
    for i in range (n):
        if i == 0 or nums[i] != nums[i-1]:
            result.append(nums[i])
    return result

a =[1, 2, 3, 2, 1]
b =[3, 2, 2, 3, 3, 2]

print(distinctarr(a,b))
