'''Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.'''
def getSecondLargest( arr):
        # Code Here
        second_larget=-1
        largets=arr[0]
        if len(arr)<2:
             return -1
        for num in arr:
               if num > largets:
                    second_larget=largets
                    largets=num
               elif num < largets and num > second_larget:
                     second_larget=num
        return second_larget


arr=[12, 35, 1, 10, 34, 1]
res=getSecondLargest(arr)
print(res)